LOCAL CGI Script for Rest Services: Postgres to JSON

developed on cloud9 >> Basic Ubuntu Workspace (Blank)
------------------

1 - Start Postgres Service

    sudo service postgresql start
    
2 - set postgre db

    https://community.c9.io/t/setting-up-postgresql/1573

    psql
    ubuntu=# CREATE DATABASE "mydb";
    ubuntu-# \password ubuntu
    Enter new password: ubuntu123
    
3 - Create a table

    ubuntu=#\c mydb
    mydb=#CREATE TABLE mytable (id serial, name text);
    
4 - Insert some data

    mydb=#INSERT INTO mytable (id,name) VALUES (0,'Duccio');
    
5 - Set DB connection in rest.py

    07#  DBNAME = 'mydb'
    08#  HOST = 'localhost'
    09#  USER = 'ubuntu'
    10#  PASSWORD = 'ubuntu123'
    
5 - Start the CGI Script for Local Rest Service Server (set PORT in server.py)

    python server.py
    
6 - Test the JSON response from an other Terminal:

    eg call the table we created before:
    
    curl 'http://localhost:8888/rest.py?type=tab&schema=public&obj=mytable'
    
    will print
    
    [
      {
        "id": 0, 
        "name": "Duccio"
      }
    ]
    
    eg call a function that list all people that see green:
    
        First we add the column and we add some more data to the DB
        
        psql
        ubuntu=#\c mydb
        mydb=#ALTER TABLE mytable ADD COLUMN vision text;
        mydb=#UPDATE mytable set vision='green' WHERE name='Duccio';
        mydb=#INSERT INTO mytable (id,name,vision) VALUES (1,'Sorrenti','ocra');
        mydb=# CREATE OR REPLACE FUNCTION f_people_colorvision(color text) RETURNS TABLE(id int, name text) AS $$ SELECT id,name from mytable WHERE vision=$1 $$ LANGUAGE SQL; 

        then we test the Rest Call from terminal
        
        curl "http://localhost:8888/rest.py?type=fun&schema=public&obj=f_people_colorvision&params=(color:'green')"
    
        that will print
        
        [
          {
            "id": "0", 
            "name": "Duccio"
          }
        ]
    
url - parameters:
    
    - type = tab (or) fun  //tab to call tables or views, fun to call functions
    
    - schema = schema_name // eg.public default postgres schema
    
    - obj = table_name (or) view_name (or) function_name
    
    - params = (param1:val1, param2:val2, ... paramN:valN)  //Optional definition of function parameters
