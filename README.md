Executing queries using Python: pythonpresto.py
===============================================

This is a sample python script showing how to run queries on Ampool Presto query engine.

Prerequisites:
--------------
Install python presto client on the machine from you want to execute queries.
Use command: 'pip install presto-client'

Usage:
------

Copy .py file to any machine from where you want to execute query.
Before running the script, you have to update connection details in the script.

'host': Ampool engine master hostname
'user': User name for Presto user. Default: 'admin'
'catalog': Presto catalog within Ampool engine. Default: 'ampool'
'schema': Presto schema within the catalog. Default: 'default'

Note: You can use above default values for 'catalog' and 'schema' and still can execute queries on other catalogs and schemas by specifying fully qualified name for the table.
For example: select * from snowflake.public.nation;

'http_scheme': 'https' for secure communication
'auth': Update Presto user name and password

After above updates, script can be simply run as: 'python pythonpresto.py'

The script has 6 sample queries:
1. CREATE TABLE tab1 (a int, b int, c varchar)
2. INSERT INTO tab1 VALUES (1, 3, 'abc')
3. INSERT INTO tab1 VALUES (4, 6, \'def\')
4. SELECT * FROM tab1
5. SELECT cast(a as varchar) as a, cast(b as double) as b, upper(c) as c FROM tab1
6. DROP TABLE tab1

======================================================================================================================================

Executing queries using JDBC: JDBCPresto.java
=============================================

This is a sample java class file showing how to run queries on Ampool Presto query engine via JDBC.

Prerequisites:
--------------
- Java 8
- Presto JDBC driver. This can be downloaded from: https://s3-us-west-2.amazonaws.com/ampool-ae2.3/AE-2.3.B17/ADM3/presto-jdbc-330.jar

Usage:
------

Copy .java file to any machine from where you want to execute query.
Before running the java program, you have to update connection details in the file.

"user" property: Provide Presto user name
"password" property: Provide Presto user password
Connection url "jdbc:presto://<AE master node>:9295/ampool/default": Provide Ampool Engine master node ip.
Query string "sql": "show catalogs"

After above updates, Java program can be executed as follows:

javac JDBCPresto.py
java -cp $CLASSPATH:<Path to downloaded Presto JDBC jar>/presto-jdbc-330.jar JDBCPresto

======================================================================================================================================

Executing queries using Presto CLI
==================================

Prerequisites:
--------------
- Java 8
- Presto CLI executable jar. This can be downloaded from: https://s3-us-west-2.amazonaws.com/ampool-ae2.3/AE-2.3.B17/ADM3/presto-cli-330-executable.jar

Usage:
------

Execute following command which will open Presto CLI.

java -jar <Path to downloaded Presto CLI jar>/presto-cli-executable.jar --server https://<AE master node hostname>:9295 --insecure --catalog ampool --schema default --user admin --password

=====================================================================================================================================
