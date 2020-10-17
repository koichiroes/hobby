#! /bin/bash

poetry run pre-commit install -c .pre-commit-config.yaml
poetry install
