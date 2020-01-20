#!/bin/bash

docker build -t door-component .
docker run -it --rm -p 8000:5000 door-component