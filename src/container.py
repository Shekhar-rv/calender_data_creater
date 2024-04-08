from psycopg2 import connect
from psycopg2.extensions import connection


postgres_connection = None

def get_pg_connection(postgres_uri: str) -> connection:
    global postgres_connection
    if postgres_connection is None:
        print("Establishing connection...")
        pg_uri = postgres_uri.split("?schema")[0]
        try:        
            postgres_connection = connect(pg_uri)
            postgres_connection.autocommit = True
            print("Connection established!")
        except Exception as e:
            print("Error: Could not establish connection")
            print(e)
    return postgres_connection