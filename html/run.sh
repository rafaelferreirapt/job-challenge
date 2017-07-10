#!/usr/bin/env bash
docker rm -f emails-html
docker build -t binaryedge/emails-html .
docker run -d --name emails-html -p 8080:80 binaryedge/emails-html