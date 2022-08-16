import uuid


class Vacancy:

    """
    Class represents vacancy model
    """

    def __init__(self, title, city, info, link, language, area, position,
                 experience, company_name, country, salary, remote, is_actual) -> None:

        self.id_ = uuid.uuid4()
        self.title = title
        self.info = info
        self.language = language
        self.area = area
        self.position = position
        self.experience = experience
        self.company_name = company_name
        self.country = country
        self.city = city
        self.salary = salary
        self.remote = remote
        self.link = link
        self.is_actual = is_actual

    def to_print(self):
        return self.title + '\n' + self.info + '\n' + self.link
