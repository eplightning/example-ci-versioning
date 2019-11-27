FROM python:3.7-slim-buster

COPY next-version.py /usr/local/bin/next-version
COPY requirements.txt /tmp/requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends git curl ssh-client && rm -rf /var/lib/apt/lists/* && \
    pip3 install -r /tmp/requirements.txt && rm /tmp/requirements.txt && \
    chmod +x /usr/local/bin/next-version

