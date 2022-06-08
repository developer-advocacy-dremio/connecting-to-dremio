#----------------------------------
# IMPORTS
#----------------------------------
## Import Pyarrow
from pyarrow import flight
from pyarrow.flight import FlightClient

## import pandas
import pandas as pd

## Import Time
import time

## get configurations from config.json
from getConfig import getConfig
config = getConfig()

#----------------------------------
# Setup
#----------------------------------

## Headers for Authentication
headers = [
    (b"authorization", f"bearer {config.get('personalKey', 'oops')}".encode("utf-8"))
    ]

## Create Client
client = FlightClient(location=("grpc+tls://data.dremio.cloud:443"))

#----------------------------------
# Function Definitions
#----------------------------------

## makeQuery function
def make_query(query, client, headers):
    
    sbegin = time.time()
    
    ## Get Schema Description and build headers #############
    flight_desc = flight.FlightDescriptor.for_command(query)
    options = flight.FlightCallOptions(headers=headers)
    schema = client.get_schema(flight_desc, options)
    #########################################################
    send = time.time()
    schema_time = send-sbegin

    
    sbegin = time.time()
    ## Get ticket to for query execution, used to get results
    flight_info = client.get_flight_info(flight.FlightDescriptor.for_command(query), options)
    #########################################################
    send = time.time()
    ticket_time = send-sbegin
    
    sbegin = time.time()
    
    ## Get Results ############################################### 
    results = client.do_get(flight_info.endpoints[0].ticket, options)
    ############################################################
    send = time.time()
    results_time = send-sbegin
    return [results, schema_time, ticket_time, results_time]

#----------------------------------
# Run Query
#----------------------------------

begin = time.time() # Start Clock
results = make_query("SELECT * FROM \"@dremio.demo@gmail.com\".\"nyc-taxi-data\" limit 1000000", client, headers)
end = time.time() # End Clock
query_time=end-begin

begin = time.time() # Start Clock
print(results[0].read_pandas())
end = time.time() # End Clock
conversion_time=end-begin

print(f"Query step 1/3 - Get Schema: {results[1]} seconds")
print(f"Query step 2/3 - Get Ticket: {results[2]} seconds")
print(f"Query step 3/3 - Get Results: {results[3]} seconds")
print(f"Full Query Completed in {query_time} seconds")
print(f"conversion to pandas Completed in {conversion_time} seconds")
print(f"Total Time: {query_time + conversion_time} seconds")