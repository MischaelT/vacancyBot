from backend.data.vacancy_data_manager import Vacancies_manager
from backend.data.parsers.sources.base_source import BaseSource

from bs4 import BeautifulSoup


class WorkUaSource(BaseSource):

    def __init__(self, manager:Vacancies_manager) -> None:

        self.manager = manager
        super().__init__()


    def parse_content(self, content: str, basepoint: str, language: str, experience: str) -> None:  # noqa

        pass
        
# def parse_workUa_data(content, basepoint) -> None:

#     soup = BeautifulSoup(content, 'html.parser')
#     vacancies = soup.find_all('div', class_='card card-hover card-visited wordwrap job-link')

#     for vacancy in vacancies:

#         title = vacancy.find('h2').text.strip()
#         info = vacancy.find('p', class_='overflow text-muted add-top-sm cut-bottom').text.strip()
#         link = basepoint + vacancy.find('a', class_='no-decoration')['href']
#         # remote = vacancy.find('span', class_ = "icon icon-home_work").next_sibling.text.strip()
#         # parsed_info_salary = self.__parse_workUa_vacancy(link)

#         # info = parsed_info_salary['info']
#         # salary = parsed_info_salary['salary']
#         salary = ''
#         data = {'title': title, 'city': '', 'info': info, 'link': link, 'salary': salary}

#     return data

# async def parse_workUa_vacancy(self, link) -> dict:

#     response = requests.get(link, headers=self.headers)

#     response.raise_for_status()

#     soup = BeautifulSoup(response.text, 'html.parser')

#     result = {}

#     try:
#         info = soup.find('div', id='job-description').text
#     except AttributeError:
#         info = ''

#     result['info'] = info

#     try:
#         salary = soup.find('b', class_='text-black').text
#     except AttributeError:
#         salary = ''

#     result['salary'] = salary

#     return result
