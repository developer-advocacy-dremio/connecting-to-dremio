## Getting Data from Dremio (in progress)

In this repository you'll find scripts on how to get data from Dremio using Dremio's REST API, ODBC and Arrow in different programming languages. The default scripts are designed to capture the time for these requests.

**NOTE: Make sure you have the right C++ libraries for ODBC and turbodbc to work correctly, these are listed here: https://turbodbc.readthedocs.io/en/latest/pages/getting_started.html

- go [here to download](https://docs.dremio.com/cloud/client-applications/dremio-drivers/) and install odbc drivers 

## Methods for Connecting to Dremio

- [Rest API]()
- [ODBC]()
- [Arrow Flight]()

## Troubleshooting Tips

#### For ODBC

- make sure unixODBC is installed
- make sure the odbc.ini and odbcinst.ini have the right driver data
- make sure autocommit is on