import json
from main_def import config_sql
import mysql.connector

config_file = config_sql
with open(config_file) as json_data_file:
    config = json.load(json_data_file)

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
ArtistUuid_from_name = 'SELECT DISTINCT artists.UUID, artists.Name FROM artists WHERE artists.Name IN ("The Reign of Kindo", "Maxi Priest", "Bob Marley", "Brett Young", "Trivium", "Cody Johnson", "Reba McEntire", "George Strait", "Brooks & Dunn", "Willie Nelson", "Chris LeDoux", "The Hives", "Yola", "Massive Attack", "Dan Auerbach", "Etta James", "The Highwomen", "The Vamps", "Bring Me The Horizon", "Elvis Costello", "Cam", "Sam Smith", "Bonnie Raitt", "SAINt JHN", "Kelsea Ballerini", "Sheryl Crow", "Halsey", "The Chainsmokers")'
mycursor.execute(ArtistUuid_from_name)
result = mycursor.fetchone()
print(result)

# import mysql.connector
# import sshtunnel
# import numpy as np
#
# with sshtunnel.SSHTunnelForwarder(
#         ssh_address_or_host=('db-proxy.vibbidi.net', 22),
#         ssh_username="ec2-user",
#         ssh_pkey='/Users/petern/Downloads/ec2-proxy2-glue-th.pem',
#         remote_bind_address=("localhost", 3306),
# ) as tunnel:
#     cnx = mysql.connector.MySQLConnection(
#         host="v4-mysql-master.vibbidi.com",
#         user="banhxeo",
#         password="rEi2019Wa-05VtJ$p",
#         database="v4",
#         port=tunnel.local_bind_port)
#     print("1")
#     cursor = cnx.cursor()
#     cursor.execute('SELECT * FROM datasources limit 10;')
#     arr = np.array(cursor.fetchall())
#     print(arr)
#     cursor.close()
#     cnx.close()
