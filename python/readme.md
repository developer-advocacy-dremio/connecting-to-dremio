To customize to your dremio instance create a config.json with the following information:

```json
{
    "personalKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==",
    "projectID": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "username": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
}
```
*personalKey = personal access token from Dremio Cloud (under account settings)

make sure to create and activate a virtual environment and install all the libraries in the requirements.txt. 

- `python -m venv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`