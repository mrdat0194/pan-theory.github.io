# from sqlalchemy import create_engine
import json
from main_def import config_sql

config_file = config_sql
with open(config_file) as json_file:
    config = json.load(json_file)

if config.get('mysql', False):
    mysql_config = config['mysql']
    RDBMS = "mysql"
    PIP_PACKAGE = "mysqlconnector"
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(
        RDBMS, PIP_PACKAGE, mysql_config['user'], mysql_config['password'],
        mysql_config['host'], mysql_config['port'], mysql_config['database'])

    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    if engine is None:
        print("failed to connect to MySQL")
        exit(1)
else:
    print("bad config file")
    exit(1)