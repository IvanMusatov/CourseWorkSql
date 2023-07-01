import json


class DataExporter:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def export_employer_data(self, employer_ids, file_path):
        employers_data = self.fetcher.get_employer_data(employer_ids)
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(employers_data, file, indent=4, ensure_ascii=False)

    def export_vacancies_data(self, employers_data, file_path):
        vacancies_data = self.fetcher.get_vacancies_data(employers_data)
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies_data, file, indent=4, ensure_ascii=False)
