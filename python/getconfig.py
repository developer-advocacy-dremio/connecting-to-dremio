import json

# Load configs from json file
def getConfig():
    with open('config.json') as file:
        return json.load(file)