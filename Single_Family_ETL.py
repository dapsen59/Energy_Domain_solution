import os
import sys
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors
import psycopg2.extras as extras
import pandas as pd
from io import StringIO
import numpy as np
from sqlalchemy import create_engine
import time


file_path = "PropertyData_R.txt"
delimiter = "|"

data_types = {
    'Account_Num': int,
    'Owner_Name': str,
    'Owner_Address': str,
    'Owner_CityState': str,
    'Owner_Zip': str,  
    'Situs_Address': str,
    'Property_Class': str
}


# ETL process starts here,  Read the text file into a Pandas DataFrame
raw_df = pd.read_csv(file_path, delimiter=delimiter, low_memory=False, dtype=data_types)

# perform transformation, selected columns needed
data = raw_df[['Account_Num', 'Owner_Name', 'Owner_Address', 'Owner_CityState', 'Owner_Zip', 'Situs_Address', 'Property_Class']]
data_types = data.dtypes


conn_params_dic = {
    "host"      : "localhost",
    "database"  : "coding_challenge",
    "user"      : "postgres",
    "password"  : "postgres"
}


# Define a function that handles and parses psycopg2 exceptions
def show_psycopg2_exception(err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()    
    # get the line number when exception occured
    line_n = traceback.tb_lineno    
    # print the connect() error
    print ("\npsycopg2 ERROR:", err, "on line number:", line_n)
    print ("psycopg2 traceback:", traceback, "-- type:", err_type) 
    # psycopg2 extensions.Diagnostics object attribute
    print ("\nextensions.Diagnostics:", err.diag)    
    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

# Using alchemy method
connect_alchemy = "postgresql+psycopg2://%s:%s@%s/%s" % (
    conn_params_dic['user'],
    conn_params_dic['password'],
    conn_params_dic['host'],
    conn_params_dic['database']
)
def using_alchemy(df):
    try:
        engine = create_engine(connect_alchemy)
        df.to_sql('tarrant_residential', con=engine, index=False, if_exists='append',chunksize = 1000)
        print("Data inserted using to_sql()(sqlalchemy) done successfully...")
    except OperationalError as err:
        # passing exception to function
        show_psycopg2_exception(err)

# Connect to the database
engine = create_engine(connect_alchemy)

# Importing data using_alchemy method
start_time = time.time()
using_alchemy(data)

end_time = time.time()


print("Time taken to load data into the database:", end_time - start_time, "seconds")
data_df = pd.read_sql_table("tarrant_residential",con=engine)
print (data_df.head())