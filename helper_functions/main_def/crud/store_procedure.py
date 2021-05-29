from sqlalchemy.dialects import mysql
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import func, union, distinct, desc
from main_def.sql_con.sqlalchemy_create_engine import SQLALCHEMY_DATABASE_URI
import pandas as pd

engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(SQLALCHEMY_DATABASE_URI))

query = '''select so.name, sc.text
from dbo.syscomments sc
         join dbo.sysobjects so on sc.id = so.id
where so.name not like 'DF__%';'''

df = pd.read_sql(query, engine)

df['text'].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=[" "," "], regex=True, inplace=True)

df_insert = df[df['text'].str.lower().str.contains("insert")]

df_view = df[df['text'].str.lower().str.contains("create view")]

df.to_csv("../adHoc/stored_procedure.csv")