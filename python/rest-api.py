#----------------------------------
# IMPORTS
#----------------------------------

## time library for measuring length of request
import time
## http client library
import requests

## get configurations from config.json
from getconfig import getConfig
config = getConfig()

#----------------------------------
# SETUP
#----------------------------------

## Credentials Setup
control_plane="https://api.dremio.cloud/v0"
auth_token = config.get("personalKey", "personalKey missing in config.json")

## Request Setup
endpoint=f"/projects/{config.get('projectID', 'projectID missing')}/sql"
url = control_plane + endpoint
headers={"authorization": f"bearer {auth_token}", "Content-Type": "application/json"}
data='{"sql": "SELECT * FROM \\"nyc-taxi-data\\" limit 100", "context":["@dremio.demo@gmail.com"] }'


#----------------------------------
# Make API Request
#----------------------------------

begin = time.time()
## request
r = requests.post(url, headers=headers, data=data)
print(r.text)
end = time.time()

print(f"REST API length of time: {end - begin}")