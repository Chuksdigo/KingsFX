
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from sqlalchemy import create_engine


def get_api_key():

     '''
     This is a function that returns the XECD API credentials from .env file.

     Parameter: Null
     Return value: A tuple of api id and api key

     Return type: tuple
     '''
     load_dotenv()
     api_key = os.getenv('API_KEY')
     api_id = os.getenv('API_ID')

     return(api_key, api_id)


def get_database_conn():

    '''
    This is a function that retrieves connection credentials from a .env file and return a postgres sqlalchemy engine

    Parameter: None
    Return Value: A Sqlalchemy engine
    Return Type: A Sqlalchemy engine object
    '''
    # Get database credentials from environment variable

    load_dotenv()
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_port = os.getenv('DB_PORT')

    # Create  and return a postgresql database connection object
    return create_engine(f'postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

