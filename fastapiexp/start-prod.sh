#! /bin/bash

gunicorn fastapiexp.api.main:app -w 2 -u app \
  -b 0.0.0.0:8000 \
  -k uvicorn.workers.UvicornWorker \
  --access-logfile -
