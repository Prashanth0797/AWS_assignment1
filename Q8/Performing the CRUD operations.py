import psycopg2

host= 'ostgresqlinstanceidentifier.xxxxxxxxxx.eu-west-3.rds.amazonaws.com'
database = 'PostgreSQLDBInstance'
user= 'admin_user'
password= 'qwert%E'

db ={}
db[host] = 'ostgresqlinstanceidentifier.xxxxxxxxxx.eu-west-3.rds.amazonaws.com'
db[database] = 'PostgreSQLDBInstance'
db[user] = 'admin_user'
db[password] = 'qwert%E'

commands = (
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL
        ) 
        """,
        """
        INSERT INTO users(user_name) VALUES ('abc')
        """,
        """
        UPDATE users
              SET user_name = 'lmn' 
              WHERE user_id = 'abc' 
        """,
        """
        DELETE FROM users WHERE user_id = 'abc'
        """


)

conn = None
try:
    conn = psycopg2.connect(db)
    cur = conn.cursor()
    for command in commands:
        cur.execute(command)

    cur.close()

    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

