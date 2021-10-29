import mysql.connector
import json

# reading connection configuration from the file
with open('database_config.txt') as f:
  data = f.read()

# reconstructing the data as a dictionary
string_config = json.loads(data)

#pass configuration to connect with mysql
cnx = mysql.connector.connect(**string_config)
cursor = cnx.cursor()