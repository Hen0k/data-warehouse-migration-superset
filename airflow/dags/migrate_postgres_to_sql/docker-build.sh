#!/bin/bash

docker build --rm -t pneuma/data_migration .

docker tag pneuma/data_migration:latest pneuma/data_migration:v1.0.0