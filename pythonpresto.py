import presto
from presto import transaction
with presto.dbapi.connect(
    host='<AE master node ip>',
    port=9295,
    user='admin',
    catalog='ampool',
    schema='default',
    http_scheme='https',
    auth=presto.auth.BasicAuthentication("admin", "admin"),
    #isolation_level=transaction.IsolationLevel.REPEATABLE_READ,
) as conn:
  conn._http_session.verify = False
  cur = conn.cursor()  

  cur.execute('CREATE TABLE tab1 (a int, b int, c varchar)')
  rows = cur.fetchall()
  print rows

  cur.execute('INSERT INTO tab1 VALUES (1, 3, \'abc\')')
  rows = cur.fetchall()
  print rows

  cur.execute('INSERT INTO tab1 VALUES (4, 6, \'def\')')
  rows = cur.fetchall()
  print rows
  
  cur.execute('SELECT * FROM tab1')
  rows = cur.fetchall()
  print rows
  
  cur.execute('SELECT cast(a as varchar) as a, cast(b as double) as b, upper(c) as c FROM tab1')
  rows = cur.fetchall()
  print rows

  cur.execute('DROP TABLE tab1')
  rows = cur.fetchall()
  print rows
