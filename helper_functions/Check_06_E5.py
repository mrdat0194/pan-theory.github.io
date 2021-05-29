import urllib.request, json
from main_def import config_sql

# with urllib.request.urlopen('https://itunes.apple.com/lookup?id=1442021816&entity=album&country=us&limit=1000') as url:
#     data = json.loads(url.read().decode())
#     print(data)


linkRequest = urllib.request.urlopen('https://itunes.apple.com/lookup?id=1442021816&entity=album&country=us&limit=1000')
linkRequest.getheaders()

# https://itunes.apple.com/lookup?id=1442021816&entity=album&country=us&limit=1000
# https://itunes.apple.com/lookup?id=1463652891&entity=album&country=us&limit=1000
# https://itunes.apple.com/lookup?id=1484688048&entity=album&country=us&limit=1000
# https://itunes.apple.com/lookup?id=1123076757&entity=album&country=us&limit=1000
# https://itunes.apple.com/lookup?id=1129446206&entity=album&country=us&limit=1000
# https://itunes.apple.com/lookup?id=1498271578&entity=album&country=us&limit=1000
# https://itunes.apple.com/lookup?id=1440766057&entity=album&country=us&limit=1000
# https://itunes.apple.com/lookup?id=1537431752&entity=album&country=us&limit=1000
# https://itunes.apple.com/lookup?id=1464346818&entity=album&country=us&limit=1000
# https://itunes.apple.com/lookup?id=1443088751&entity=album&country=us&limit=1000

config_file = config_sql
with open(config_file) as json_data_file:
    config = json.load(json_data_file)
import mysql.connector

if config.get('mysql', False):
    mysql_config = config['mysql']
    mydb = mysql.connector.connect(
        host=mysql_config['host'],
        user=mysql_config['user'],
        password=mysql_config['password'],
        database=mysql_config['database'],
        port=mysql_config['port']
    )

mycursor = mydb.cursor()
query = f'''SELECT distinct albums.*
FROM crawlingtasks b
JOIN albums on albums.ItuneAlbumId = b.TaskDetail ->> "$.album_id"
WHERE b.TaskDetail ->> '$.album_id' IN ("1442021816",
                                        "1463652891",
                                        "1484688048",
                                        "1123076757",
                                        "1129446206",
                                        "1498271578",
                                        "1440766057",
                                        "1537431752",
                                        "1464346818",
                                        "1443088751")
  AND b.ActionId = "9C8473C36E57472281A1C7936108FC06"
  AND b.Status = 'incomplete';'''

mycursor.execute(query)
result = mycursor.fetchall()
print(result)

# cd /Users/petern/opt/anaconda3/bin
# source activate root
# cd
# source activate /Users/petern/opt/anaconda3/envs/py3-TF2.0
# export PATH=${PATH}:/usr/local/mysql/bin