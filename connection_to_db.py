import psycopg2 as ps

conn2 = ps.connect(dbname = 'postgres',
                  user = 'postgres',
                  password = '123456',
                  host = 'localhost',
                  port = '5432')
