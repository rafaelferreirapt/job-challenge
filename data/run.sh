#!/usr/bin/env bash
docker rm -f elastic
docker pull elasticsearch
docker run -p 9200:9200 -e "http.host=0.0.0.0" -e "transport.host=127.0.0.1" --name elastic -d elasticsearch
cd raw
pip install -r requirements.txt
echo "waiting for elastic search"
python read.py
cd ..