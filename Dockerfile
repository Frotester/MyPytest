FROM python:3.9-alpine

ARG run_env=development
ENV env $run_env

LABEL "channel"="SolveMe"
LABEL "creator"="SolveMe community"

WORKDIR ./usr/lessons

COPY . .

RUN apk update && apk upgrade && apk add bash

RUN pip3 install -r requirements.txt

CMD pytest -m "$env" -s -v tests/*