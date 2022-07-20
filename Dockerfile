FROM alpine:3.14
RUN apk add python3
RUN apk add py3-pip
RUN apk add net-snmp
RUN apk add net-snmp-tools
ADD . /code
WORKDIR /code
RUN python3 -m pip install -r /code/requirements.txt

CMD uvicorn oidman:app --reload --port 9002 --host "0.0.0.0"