# Energy_Domain_solution
ETL Script For Residential Property Dataset 
The ETL code works using postgres local installation or docker compose instance however changes to the database connection is needed. Plug in your username and database password and you should be good
Also, Ensure that the database "coding_challenge" and the table "tarrant_residential" is created in your environment, both scripts needed to create database and table  are include in this repository. 

conn_params_dic = {
    "host"      : "localhost",
    "database"  : "coding_challenge",
    "user"      : "postgres",
    "password"  : "postgres"
}

To run the main ETL script (Single_Family_ETL) Please ensure the data file (PropertyData_R.txt) is in the same folder/directory as the ETL script. I am unable to include the data file due to my github size restriction.

Also, I have included two scripts to extract (sql_query_script_to_df, sql_query_to_df) to extract five corporate entities which own the greatest number of single-family residential properties, 
"sql_query_script_to_df" does job better but feel free to run both. 
