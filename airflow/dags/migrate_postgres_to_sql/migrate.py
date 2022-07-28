from postgresql_manager import get_trajectories, get_vehicles
from mysql_manager import (
    mysql_create_tables,
    mysql_get_table_names,
    mysql_insert_data
)


def migrate_data():
    # Create the table on MySQL
    mysql_create_tables()
    print("Tables created on MySQL")
    # Get the data from Postgres
    trajectories_df = get_trajectories()
    vehicles_df = get_vehicles()
    # print(trajectories_df.info())
    # print(vehicles_df.info())
    print("Got the data from PostgrSQL")
    # Dump data to MySQL
    
    
    mysql_insert_data(trajectories_df, "trajectories")
    mysql_insert_data(vehicles_df, "vehicles")
    tables = mysql_get_table_names()
    print(f"{tables} are inserted to MySQL")



if __name__=="__main__":
    migrate_data()