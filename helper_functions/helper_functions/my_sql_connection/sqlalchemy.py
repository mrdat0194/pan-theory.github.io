from sqlalchemy import create_engine
import json
from main_def import config_sql
import urllib
import pandas as pd

config_file = config_sql
with open(config_file) as json_file:
    config = json.load(json_file)

if config.get('sqlserver_bm', False):

    mssql_config = config['sqlserver_bm']
    server = mssql_config['host']
    database = mssql_config['database']
    username = mssql_config['user']
    password = mssql_config['password']

    SQLALCHEMY_DATABASE_URI = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                                     "SERVER="+server+";"
                                     "DATABASE="+database+";"
                                     "UID="+username+";"
                                     "PWD="+password)

    engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(SQLALCHEMY_DATABASE_URI))

    # engine = create_engine(SQLALCHEMY_DATABASE_URI)
    if engine is None:
        print("failed to connect to MySQL")
        exit(1)
    else:
        query = 'SELECT Top 3 * FROM Users'
        df = pd.read_sql(query, engine)
        print(df)
else:
    print("bad config file")
    exit(1)


