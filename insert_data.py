import os


class InsertData:
    '''Реализация заполнения БД данными из файлов'''

    def __init__(self, db):
        self.db = db

    def insert_employer_data(self, employer_data):
        file_path = os.path.join(os.getcwd(), 'queries.sql')
        with open(file_path, 'r', encoding='utf-8') as f:
            queries = f.read().split(';')
            query = queries[2].strip()  # Запрос для вставки данных о работодателях
            for employer in employer_data:
                values = (
                    employer['id'],
                    employer['name'],
                    employer.get('address', ''),
                    employer.get('site_url', '')
                )
                self.db.execute_query(query, values)

    def insert_vacancies_data(self, vacancies_data):
        file_path = os.path.join(os.getcwd(), 'queries.sql')
        with open(file_path, 'r', encoding='utf-8') as f:
            queries = f.read().split(';')
            query = queries[3].strip()  # Запрос для вставки данных о вакансиях
            for vacancy in vacancies_data:
                values = (
                    vacancy['vacancy_id'],
                    vacancy['company_id'],
                    vacancy['name'],
                    vacancy.get('salary_from'),
                    vacancy.get('salary_to')
                )
                self.db.execute_query(query, values)
