FROM python:3.12.3-slim-bookworm

WORKDIR /app

COPY . /app/

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install git

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]

