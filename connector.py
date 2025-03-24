from psycopg2 import connect

import configparser
import os

if not(os.path.exists("config.ini")):
    host = input("Host: ")
    port = input("Port: ")
    database = input("Database: ")
    user = input("User: ")


    config = configparser.ConfigParser()
    config['credentials'] = {'host':host, 
                             'port':port,
                             'database':database,
                             'user':user}
    
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

else:
    config = configparser.ConfigParser()
    config.read('config.ini')

    host = config.get('credentials', 'host')
    port = config.get('credentials', 'port')
    database = config.get('credentials', 'database')
    user = config.get('credentials', 'user')


password = input("Password: ")

try:
    conn = connect(host=host, port=port, database=database, user=user, password=password)

    print('connection established')

    table = input("Table Name: ")

    with conn.cursor() as cur:
        # Example query: SELECT * FROM stuff LIMIT 5;

        # Not sanitized, but its just a little script so it doesn't matter.
        query = f"SELECT * FROM {table} LIMIT 5;"
        cur.execute(query)
        
        data = cur.fetchall()
        print(f"Data fetched: {data}")
        
        # Close the cursor and connection
        cur.close()
        conn.close()

except Exception as e:
    print(f"Error connecting to the database: {e}")
