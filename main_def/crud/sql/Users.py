from main_def.models.Users import Users
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import func, union, distinct, desc
from main_def.sql_con.sqlalchemy_create_engine import SQLALCHEMY_DATABASE_URI

engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(SQLALCHEMY_DATABASE_URI))

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_users(UserIDquery : tuple):
    Users_Info = (db_session.query(Users.UserID,
                                   Users.Username,
                                   Users.Email,
                                   Users.DisplayName
                                   )
                  .select_from(Users)
                  .filter(Users.UserID.in_(UserIDquery))
                  )
    return Users_Info

if __name__ == '__main__':
    users_ids = ['1', '3']
    user_info = get_users(users_ids)
    for user in user_info:
        email = user.DisplayName
        print(email)
