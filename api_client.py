import requests


class HHDataFetcher:
    def __init__(self):
        self.base_url = 'https://api.hh.ru'

    def get_employer_data(self, employer_ids):
        employers_data = []

        for employer_id in employer_ids:
            api_url = f'{self.base_url}/employers/{employer_id}'

            try:
                response = requests.get(api_url)
                employer_data = response.json()

                employer_info = {
                    'id': employer_data.get('id'),
                    'name': employer_data.get('name'),
                    'site_url': employer_data.get('site_url'),
                    'open_vacancies': employer_data.get('open_vacancies')
                }

                employers_data.append(employer_info)
            except requests.exceptions.RequestException as error:
                print(f'Error while fetching employer data for employer ID {employer_id}:', error)

        return employers_data

    def get_vacancies_data(self, employers_data):
        vacancies_data = []

        for employer_info in employers_data:
            employer_id = employer_info['id']
            api_url = f'{self.base_url}/vacancies?employer_id={employer_id}'

            try:
                response = requests.get(api_url)
                vacancies = response.json().get('items')

                for vacancy in vacancies:
                    salary = vacancy.get('salary')
                    salary_from = salary.get('from') if salary else None
                    salary_to = salary.get('to') if salary else None

                    vacancy_info = {
                        'company_id': employer_info['id'],
                        'vacancy_id': vacancy.get('id'),
                        'name': vacancy.get('name'),
                        'salary_from': salary_from,
                        'salary_to': salary_to
                    }

                    vacancies_data.append(vacancy_info)
            except requests.exceptions.RequestException as error:
                print(f'Error while fetching vacancies data for employer ID {employer_id}:', error)

        return vacancies_data
