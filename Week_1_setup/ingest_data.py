import argparse
import pandas as pd
import os
import gzip
from time import time
from sqlalchemy import create_engine


def main(params):
    User = params.User
    Password = params.Password
    Host = params.Host
    Port = params.Port
    Database = params.Database
    Table_Name = params.Table_Name
    url = params.url
    csv_name = 'output.csv'

    os.system(f"wget -o {csv_name} {url}")

    # Gunzip the file
    decompressed_file = 'output_decompressed.csv'
    with gzip.open(csv_name, 'rb') as file_in:
        with open(decompressed_file, 'wb') as file_out:
            file_out.write(file_in.read())

    engine = create_engine(f'postgresql://{User}:{Password}@{Host}:{Port}/{Database}')

    df_iter = pd.read_csv(decompressed_file, iterator=True, chunksize=100000)

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=Table_Name, con=engine, if_exists='append')

    df.to_sql(name=Table_Name, con=engine, if_exists='append')

    while True:
        t_start = time()

        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=Table_Name, con=engine, if_exists='append')

        t_end = time()

        print('Inserting another chunk..., took %.3f seconds' % (t_end - t_start))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to PostgreSQL')

    parser.add_argument('--User', help='User name for PostgreSQL')
    parser.add_argument('--Password', help='Password for PostgreSQL')
    parser.add_argument('--Host', help='Host for PostgreSQL')
    parser.add_argument('--Port', help='Port for PostgreSQL')
    parser.add_argument('--Database', help='Database for PostgreSQL')
    parser.add_argument('--Table_Name', help='Name of the table where the data will be written')
    parser.add_argument('--url', help='URL of the CSV file')

    args = parser.parse_args()

    main(args)
