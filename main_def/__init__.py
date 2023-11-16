import os

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
query_path = os.path.join(MAIN_DIR, "info", "query.txt")
data_trial = os.path.join(MAIN_DIR, "data", "Gonj")
config_sql = os.path.join(MAIN_DIR, "sql_con", "database.json")
credentials = os.path.join(MAIN_DIR, "ggl_api", "kasa", "GoogleAds", "credentials.json")
tokens = os.path.join(MAIN_DIR, "ggl_api", "token.pickle")

# function_utils = os.path.join(MAIN_DIR,"Complete_Function.py")
# exec(open(function_utils).read())

