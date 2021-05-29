from sqlalchemy import create_engine
import json
from main_def import config_sql
import urllib
import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", 50, 'display.width', 1000)

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

if __name__ == '__main__':

    engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(SQLALCHEMY_DATABASE_URI))

    if engine is None:
        print("failed to connect to MySQL")
        exit(1)
    else:
        # query = 'SELECT Top 3 * FROM Users'
        # df = pd.read_sql(query, engine)
        # print(df)
        with engine.begin() as conn:
            # result = conn.execute('EXEC dbo.simpleSelect')
            # for row in result:
            #     print(row)

            result = conn.execute('dbo.simpleString ?, ?', ['Dat', 'Nguyen'])
            print(result)
            for row in result:
                print(row)


