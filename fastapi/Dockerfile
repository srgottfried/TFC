FROM python:3.12.0b1-slim-buster
RUN apt update && apt -y upgrade
RUN pip install fastapi uvicorn
RUN mkdir /fastapi
COPY surveillance_api.py /fastapi
WORKDIR /fastapi
CMD ["uvicorn", "surveillance_api:app", "--host", "0.0.0.0", "--port", "8000"]