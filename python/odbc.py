#----------------------------------
# IMPORTS
#----------------------------------

## Import Time
import time

## Import pyodbc
import pyodbc

## import pandas
import pandas as pd

## get configurations from config.json
from getConfig import getConfig
config = getConfig()

#----------------------------------
# SETUP
#----------------------------------

token=config.get("personalKey", "personalKey missing from config.json")
connector="Driver={Dremio ODBC Driver 64-bit};ConnectionType=Direct;HOST=sql.dremio.cloud;PORT=443;AuthenticationType=Plain;" + f"UID=$token;PWD={token};ssl=true;"

#----------------------------------
# CREATE CONNECTION AND CURSOR
#----------------------------------

# establist connection
cnxn = pyodbc.connect(connector, autocommit=True)

# set encoding
cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')

# creating a cursor to send messages through the connection
cursor = cnxn.cursor()

#----------------------------------
# RUN QUERY
#----------------------------------

## Start Clock
begin = time.time()

## run a query
rows = cursor.execute("SELECT * FROM \"@dremio.demo@gmail.com\".\"nyc-taxi-data\" limit 1000000").fetchall()

end = time.time()
query_time=end-begin


begin = time.time()
print(pd.DataFrame([tuple(t) for t in rows]))

## End Clock Clock
end = time.time()

conversion_time=end-begin


## Print time it took
print(f"took {query_time} seconds to execute query")    
## Print time it took
print(f"took {conversion_time} seconds to convert to pandas")
print(f"Total Time: {query_time + conversion_time} seconds")