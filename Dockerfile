FROM python:3.9-alpine

# ARG run_env=development
# ENV env $run_env

LABEL "channel"="SolveMe"
LABEL "creator"="SolveMe community"

WORKDIR ./usr/lessons

VOLUME /allureResults

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD pytest -s -v tests/* --alluredir=allureResults