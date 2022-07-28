import os
from pprint import pprint
from traceback import print_exc
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import inspect
from dotenv import load_dotenv

load_dotenv()


# Connect to your PostgreSQL database on a remote server
HOST = os.getenv("MYSQL_HOST")
PORT = os.getenv("MYSQL_PORT")
USER = os.getenv("DBUSER")
PASS = os.getenv("MYSQL_PASS")
DB = os.getenv("DB")

TRAJECTORY_SCHEMA = "trajectory_info_schema.sql"
VEHICLE_SCHEMA = "vehicle_info_schema.sql"
CONNECTION_STR = f"mysql+pymysql://{USER}:{PASS}@{HOST}/{DB}"
BANNER = "="*20

# Connect to the database
ENGINE = create_engine(CONNECTION_STR)

def mysql_create_tables():
    try:
        with ENGINE.connect() as conn:
            for name in [VEHICLE_SCHEMA, TRAJECTORY_SCHEMA]:
                with open(name) as file:
                    query_text = file.read()
                    query_text = query_text.replace("SERIAL", "AUTO_INCREMENT")
                    query_text = query_text.replace("ON DELETE CASCADE", "")
                    query_text = query_text.replace('"', "`")
                    
                    query = text(query_text)
                    conn.execute(query)
        print("Successfully created 2 tables")
    except:
        print("Unable to create the Tables")
        print(print_exc())


# Populate the tables
def mysql_insert_data(df: pd.DataFrame, table_name):
    try:
        with ENGINE.connect() as conn:
            df.to_sql(name=table_name, con=conn,
                      if_exists='replace', index=False)
        print(f"Done inserting to {table_name}")
        print(BANNER)
    except:
        print("Unable to insert to table")
        print(print_exc())


# Implement Querying functions
def mysql_get_table_names():
    with ENGINE.connect() as conn:
        inspector = inspect(conn)
        names = inspector.get_table_names()
        return names


def mysql_get_vehicles():
    with ENGINE.connect() as conn:
        veh_df = pd.read_sql_table('vehicles', con=conn)

        return veh_df


def mysql_get_trajectories():
    with ENGINE.connect() as conn:
        trajectories_df = pd.read_sql_table('trajectories', con=conn)

        return trajectories_df


if __name__=="__main__":
    print(mysql_get_table_names())