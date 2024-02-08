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
