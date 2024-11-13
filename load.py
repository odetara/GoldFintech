import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv(override=True)


def get_postgres_engine():
    """
    Constructs a SQLalchemy engine object for postgres DB from .env file
    
    Paremeters: None
    
    Returns:
    -sqlachemy engine (sqlalchemy.engine.Engine)
    """
    engine = create_engine("postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(
        host = os.getenv('host'),
        port = os.getenv('port'),
        user = os.getenv('user'),
        password = os.getenv('password'),
        dbname = os.getenv('database')
        )
    )
    
    return engine

def load_csv_to_postgres(csv_file_path, table_name, engine):
    """
    Loads data from a csv file to a postgres DB table
    
    Parameters:
    -csv_file_path(str): Path to csv file
    -table_name(str): a postgres table
    -engine (sqlalchemy.engine): an SQL alchemy eninge object
    -schema (str): a postgres DB schema
    """
    
    df = pd.read_csv('msftstock.csv')
    
    try:
        with engine.connect() as connection:
            df.to_sql('goldfintech', connection, index=False, if_exists='replace')
            
        print(f'{len(df)} rows successfully Loaded to Postgres DB')
    except Exception as e:
        print(f"An error occurred: {e}")    
    
engine = get_postgres_engine()
    

    

    
load_csv_to_postgres('msftstock.csv','goldfintech', engine)
    
    # execute code
session = sessionmaker(bind=engine)
session = session()
session.commit()
    
    
print('pipeline executed successfully')