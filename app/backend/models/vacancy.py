class Vacancy:

    """
    Class represents vacancy model
    """

    def __init__(self, date, title, city, info, link) -> None:

        self.date = date
        self.title = title
        self.city = city
        self.info = info
        self.link = link

    def to_print(self):

        return self.title+'\n'+self.info+'\n'+self.link
