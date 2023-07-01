import json
import os

from create_tables import CreateTable
from database import Database
from insert_data import InsertData
from get_files import DataExporter
from api_client import HHDataFetcher

# Создание файлов с компаниями и вакансиями
hh_fetcher = HHDataFetcher()
data_exporter = DataExporter(hh_fetcher)

employer_ids = ['1740', '2624085', '1942330', '4181', '49357', '78638', '3529', '1332487', '3710', '5181704']
employers_file_path = 'employers_data.json'
data_exporter.export_employer_data(employer_ids, employers_file_path)

vacancies_file_path = 'vacancies_data.json'
with open(employers_file_path, 'r', encoding='utf-8') as file:
    employers_data = json.load(file)
data_exporter.export_vacancies_data(employers_data, vacancies_file_path)

# Использование класса CreateTable
db = Database(dbname='Vacancies', user="postgres", password="123cvb89pln", host='localhost')
table_creator = CreateTable(db)
table_creator.create_tables()
db.close_connection()

# Использования класса InsertData
db = Database(dbname='Vacancies', user="postgres", password="123cvb89pln", host='localhost')
data_inserter = InsertData(db)

# Определение относительного пути к файлу с данными о работодателях
file_path = os.path.join(os.getcwd(), 'employers_data.json')

if not os.path.exists(file_path):
    print('Файл с данными о работодателях не найден.')
else:
    with open(file_path, 'r', encoding='utf-8') as f:
        employers_data = json.load(f)
        data_inserter.insert_employer_data(employers_data)

# Определение относительного пути к файлу с данными о вакансиях
file_path = os.path.join(os.getcwd(), 'vacancies_data.json')

if not os.path.exists(file_path):
    print('Файл с данными о вакансиях не найден.')
else:
    with open(file_path, 'r', encoding='utf-8') as f:
        vacancies_data = json.load(f)
data_inserter.insert_vacancies_data(vacancies_data)
db.close_connection()
