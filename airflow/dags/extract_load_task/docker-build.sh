#!/bin/bash

docker build --rm -t pneuma/eltaskdag .

docker tag pneuma/eltaskdag:latest pneuma/eltaskdag:v1.0.0