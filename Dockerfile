FROM python:3.12.3-slim-bookworm

WORKDIR /app

COPY . /app/

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install git

RUN pip3 install --user  --no-cache-dir --upgrade -r requirements.txt

# 本番環境では, --hostとして--reloadを削除する
# CMD ["uvicorn", "app.main:app", "--reload"]

