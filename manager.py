import os

import psycopg2


class DBManager:
    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, values=None):
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_companies_and_vacancies_count(self):
        file_path = os.path.join(os.getcwd(), 'queries.sql')
        with open(file_path, 'r', encoding='utf-8') as f:
            queries = f.read().split(';')
            query = queries[4].strip()
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def get_all_vacancies(self):
        file_path = os.path.join(os.getcwd(), 'queries.sql')
        with open(file_path, 'r', encoding='utf-8') as f:
            queries = f.read().split(';')
            query = queries[5].strip()
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def get_avg_salary(self):
        file_path = os.path.join(os.getcwd(), 'queries.sql')
        with open(file_path, 'r', encoding='utf-8') as f:
            queries = f.read().split(';')
            query = queries[6].strip()
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def get_vacancies_with_higher_salary(self):
        avg_salary = self.get_avg_salary()
        file_path = os.path.join(os.getcwd(), 'queries.sql')
        with open(file_path, 'r', encoding='utf-8') as f:
            queries = f.read().split(';')
            query = queries[7].strip()
        self.cursor.execute(query, avg_salary)
        results = self.cursor.fetchall()
        return results

    def get_vacancies_with_keyword(self, keyword):
        file_path = os.path.join(os.getcwd(), 'queries.sql')
        with open(file_path, 'r', encoding='utf-8') as f:
            queries = f.read().split(';')
            query = queries[8].strip()
        self.cursor.execute(query, ('%' + keyword + '%',))
        results = self.cursor.fetchall()
        return results

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
