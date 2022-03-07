class User():

    def __init__(self, id_, experience, language, salary) -> None:
        self. id = id_
        self.experience = experience
        self.language = language
        self.salary = salary

    def to_print(self):
        return 'Experience: '+self.experience+'\n'+'Language: '+self.language+'\n'+'Desired salary: '+self.salary
