class Vacancy:

    def __init__(self, data, title, city, info, link) -> None:
        self.data = data
        self.title = title
        self.city = city
        self.info = info
        self.link = link

    def to_print(self):
        return  self.title+'\n'+self.info+'\n'+self.link