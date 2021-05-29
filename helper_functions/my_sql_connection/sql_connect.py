import json
from main_def import config_sql
import pyodbc

config_file = config_sql
with open(config_file) as json_data_file:
    config = json.load(json_data_file)

if config.get('sqlserver_bm', False):
    mssql_config = config['sqlserver_bm']
    server = mssql_config['host']
    database = mssql_config['database']
    username = mssql_config['user']
    password = mssql_config['password']
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

mycursor = cnxn.cursor()
Users_table = 'SELECT Top 3 * FROM Users'
mycursor.execute(Users_table)
result = mycursor.fetchone()
print(result)