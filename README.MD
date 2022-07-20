# OIDMAN

#### summary
A simple ui providing fast SNMP polling one or multiple OID's (sub second if supported by your hardware).

- Built on the tried and true SNMPWalk
- Simple container deployment
- Leverages websockets for near realtime polling

#### installing
```
git clone https://github.com/tbotnz/oidman.git
cd oidman
sudo docker-compose up --build
```

you can then access oidman via ```http://localhost:9002```

#### demo
![oidman demo](/oidman.gif)


#### important note
project is experimental, we assume you know what you are doing.
