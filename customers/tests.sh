#!/bin/bash

# A simple script for testing the API with bash & curl during development. For more complete DRF tests see tests.py

echo 'Creating a user'
curl -X POST http://127.0.0.1:8000/api/customers/ -H 'Content-Type: application/json' -d '{"first_name":"billy", "last_name":"williams", "email": "billyworld@billy.com"}'

echo 'getting the customers from the API in json format'
curl http://127.0.0.1:8000/api/customers/?format=json

echo 'getting the customers form the api in API format'
curl http://127.0.0.1:8000/api/customers/?format=api

echo 'getting a customer by ID'
curl http://127.0.0.1:8000/api/customers/2/
