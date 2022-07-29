#! /bin/zsh
# This setup coad is taken from https://medium.com/geekculture/run-apache-superset-locally-in-10-minutes-30bc70ed808c

# Fetch and run the docker image
docker run -d -p 8088:8088 --name apache_superset --network "dwh-network" apache/superset 

sleep 10

# Create the Admin account
docker exec -it apache_superset superset fab create-admin \
        --username admin \
        --firstname Admin \
        --lastname Admin \
        --email admin@superset.com \
        --password admin

# Update the local database to the current version
docker exec -it apache_superset superset db upgrade

# Load the examples
# docker exec -it data_diving superset load_examples


# Initialize the newly created role
docker exec -it apache_superset superset init