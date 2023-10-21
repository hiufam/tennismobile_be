from psycopg2 import connect
import pandas as pd

from ...database import engine

postgres_conn_dict = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': '123456'
}

conn = connect(**postgres_conn_dict)

conn.set_session(autocommit=True)

csv_files = {
    'm_racket_string': r'data\racket_strings.csv',
    'm_racket_brand': r'data\racket_brands.csv',
    'm_racket_parameter': r'data\racket_parameters.csv',
    'm_clothing_brand': r'data\clothing_brands.csv',
    'm_ball_brand': r'data\ball_brands.csv',
    'm_shoes_brand': r'data\shoes_brands.csv'
}

for table_name, file_path in csv_files.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists='replace', index=False)