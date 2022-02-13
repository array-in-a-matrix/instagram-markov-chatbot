import json

with open('login.json', 'r') as file:
    json_object = json.load(file)

username = json_object['username']
password = json_object['password']
dataset = json_object['dataset']
recent = json_object['recent']
interval = json_object['interval']