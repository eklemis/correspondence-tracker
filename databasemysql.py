import mysql.connector
import json

# reading connection configuration from the file
with open('database_config.txt') as f:
  data = f.read()

# reconstructing the data as a dictionary
string_config = json.loads(data)

#pass configuration to connect with mysql
#import the cnx and cursor to your modul to interact with the project's mysql database
mysql_cnx = mysql.connector.connect(**string_config)
mysql_cursor = mysql_cnx.cursor()