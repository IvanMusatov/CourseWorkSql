import psycopg2


class Database:
    '''Реализуем подключение к БД'''

    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, values=None):
        self.cursor.execute(query, values)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
