# FastApiDocker
This repo is simple demo how to build very simple dockerized application.

## What this application does?
It builds two containers. Both will be serving fastapi service.

**squre** Has endpoint that simply returns the squareroot of the number.

**sub** Has endpoint that will call **square**'s endpoint and will substract 100 from the output.

## How to install?
Tested with Docker 24.0.5
```console
docker compose up -d
```

## How to use?
Go to http://localhost:8091/docs and use the swagger UI to check if it is working :)



