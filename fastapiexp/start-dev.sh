#! /bin/bash

poetry run uvicorn fastapiexp.api.main:app --reload
