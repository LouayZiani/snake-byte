import psycopg2

def create_tables():
    
    commands = (
        """
        CREATE TABLE IF NOT EXISTS scores (
            user_name VARCHAR(32) NOT NULL PRIMARY KEY,
            score INT NOT NULL
        )
        """,
    )
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="kooora25") as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


