from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import subprocess
import asyncio

from config import config

from datetime import datetime

import random

import re

from lookups import lookup_table

app = FastAPI()
templates = Jinja2Templates(directory="templates")


async def get_snmp(oid: str, host: str, community: str, resolve: str):
    return_result = []
    try:
        if resolve:
            result = subprocess.check_output(
                ["snmpwalk", "-v2c", "-Of", "-c", community, host, oid]
            )
        else:
            result = subprocess.check_output(
                ["snmpwalk", "-v2c", "-On", "-c", community, host, oid]
            )
        response = result.decode("utf-8").split("\n")
        for message in response:
            if message != "":
                lookups = lookup_table
                for lookup in lookups:
                    if lookup["match_str"] in message:
                        match = re.search(lookup["regexp"], message)
                        if match:
                            oid = message.split(" = ")[0]
                            return_result.append(
                                {
                                    "oid": oid,
                                    "value": lookup["type"](match.group(lookup["group"])),
                                }
                            )
    except Exception as e:
        print (e)
    return return_result


@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("template.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        for lp in range(int(data[0]["polls"])):
            result = []
            for payload in data:
                await asyncio.sleep(float(data[0]["interval"]))
                snmp_pl = await get_snmp(
                    oid=payload["oid"],
                    host=payload["host"],
                    community=payload["community"],
                    resolve=payload["resolve_oid"],
                )
                for snmp_result in snmp_pl:
                    now = datetime.now()
                    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                    result.append(
                        {
                            "message": payload,
                            "payload": snmp_result["value"],
                            "timestamp": date_time,
                            "chart_key": snmp_result["oid"] + "-" + payload["host"],
                        }
                    )
            await websocket.send_json(result)