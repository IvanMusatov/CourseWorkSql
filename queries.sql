-- Запрос для создания таблицы employers
CREATE TABLE IF NOT EXISTS employers (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    site_url VARCHAR(255)
);
-- Запрос для создания таблицы vacancies
CREATE TABLE IF NOT EXISTS vacancies (
    vacancy_id VARCHAR(255) PRIMARY KEY,
    company_id VARCHAR(255) REFERENCES employers (id),
    name VARCHAR(255),
    salary_from INTEGER,
    salary_to INTEGER
);
-- Запрос для вставки данных о работодателях
INSERT INTO employers (id, name, address, site_url)
VALUES (%s, %s, %s, %s)
ON CONFLICT DO NOTHING;

-- Запрос для вставки данных о вакансиях
INSERT INTO vacancies (vacancy_id, company_id, name, salary_from, salary_to)
VALUES (%s, %s, %s, %s, %s);

--Получение списка всех компаний и количества вакансий
SELECT employers.name, COUNT(vacancies.vacancy_id)
FROM employers
LEFT JOIN vacancies ON employers.id = vacancies.company_id
GROUP BY employers.name;

--Получение списка всех вакансий
SELECT employers.name, vacancies.name, vacancies.salary_from, vacancies.salary_to, vacancies.site_url
FROM vacancies
INNER JOIN employers ON vacancies.company_id = employers.id;

--Получение средней зарплаты по вакансиям
SELECT AVG(salary_from), AVG(salary_to)
FROM vacancies;

--Получение списка вакансий с зарплатой выше средней
SELECT employers.name, vacancies.name, vacancies.salary_from, vacancies.salary_to, vacancies.site_url
FROM vacancies
INNER JOIN employers ON vacancies.company_id = employers.id
WHERE (vacancies.salary_from > %s OR vacancies.salary_to > %s);

--Получение списка вакансий
SELECT employers.name, vacancies.name, vacancies.salary_from, vacancies.salary_to, vacancies.site_url
FROM vacancies
INNER JOIN employers ON vacancies.company_id = employers.id
WHERE vacancies.name ILIKE %s;
