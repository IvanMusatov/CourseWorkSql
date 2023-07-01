import os


class CreateTable:
    def __init__(self, db):
        self.db = db

    def create_tables(self):
        file_path = os.path.join(os.getcwd(), 'queries.sql')
        with open(file_path, 'r', encoding='utf-8') as f:
            queries = f.read().split(';')
            for query in queries[:2]:
                if query.strip():
                    self.db.execute_query(query.strip() + ';')
