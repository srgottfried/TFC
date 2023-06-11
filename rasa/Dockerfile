FROM python:3.9-slim-buster
RUN apt update && apt -y upgrade
RUN python3 -m pip install --upgrade pip
RUN mkdir /rasa
COPY requirements.txt /rasa
RUN pip install -r /rasa/requirements.txt
RUN mkdir -p /rasa/data /rasa/models /rasa/actions /rasa/utils
COPY ./data /rasa/data
COPY *.yml /rasa
COPY ./actions /rasa/actions
COPY ./utils /rasa/utils
WORKDIR /rasa
RUN rasa train
ENTRYPOINT [ "/bin/bash", "-c" ]