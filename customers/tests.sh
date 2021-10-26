# todo use framework
curl http://127.0.0.1:8000/api/customers/?format=api
curl http://127.0.0.1:8000/api/customers/?format=json

http --form POST http://127.0.0.1:8000/api/customers/ first_name="Jeff"