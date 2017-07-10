#!/usr/bin/env bash
set -e
cd data
./run.sh

pwd
cd ../api
./run.sh

pwd
cd ../html
./run.sh