To customize to your dremio instance create a config.json with the following information:

```json
{
    "personalKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==",
    "projectID": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "JDBC_string": "jdbc:dremio:direct=sql.dremio.cloud:443;ssl=true;PROJECT_ID=xxxxxxxxxxxxxxxxxxxxxxxxx;",
    "username": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "jdbcjar": "/xxxxxx/dremio-jdbc-driver-20.1.0-202202061055110045-36733c65.jar"
}
```
*personalKey = personal access token from Dremio Cloud (under account settings)

make sure to create and activate a virtual environment and install all the libraries in the requirements.txt. 

- `python -m venv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`