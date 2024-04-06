
import pandas as pd


def load_data(engine, table):
    
     '''
      This is a function that loads data to a table on postgres database

      Parameters:
        - df- a dataframe
        - engine -  a sqlalchemy engine
        - table - a database table on postgres
      Return Value: Null
      Return type: Null
     '''

     df2 = pd.read_csv('./opt/airflow/raw/df.csv')
     df2.to_sql(table, engine, if_exists='append', index=False)
     