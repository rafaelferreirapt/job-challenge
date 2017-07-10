#!/usr/bin/env bash
set -e

# get elastic search IP and update in settings

API_CONTAINER_ID=$(docker ps | grep "elastic" | awk '/ /{print $1}')
IP_ADDRESS=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $API_CONTAINER_ID)
sed -i.bu '3s/.*/ELASTIC_HOST = "'$IP_ADDRESS'"/' settings/development.py
sed -i.bu '3s/.*/ELASTIC_HOST = "'$IP_ADDRESS'"/' settings/production.py
rm settings/production.py.*
rm settings/development.py.*


docker rm -f emails-api
docker build -t binaryedge/emails-api .

rc=$?;
if [[ $rc != 0 ]];
then
exit $rc;
fi

docker run -d --name emails-api -p 5001:80 binaryedge/emails-api