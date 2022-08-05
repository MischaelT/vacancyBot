from frontend.data.consts import AREAS_LIST
from backend.data.db.choices import MANAGEMENT

class User():

    """
    Class represents user model
    """

    def __init__(self, user_id, is_registered, experience, location, salary, area, position, language) -> None:

        self.user_id = user_id
        self.is_registered = is_registered
        self.area = area
        self.position = position
        self.experience = experience
        self.language = language
        self.location = location
        self.salary = salary

    def to_print(self):

        if self.area == MANAGEMENT:

            text = f"""
            Area: {AREAS_LIST[self.area]}
            \nSpecialisation: {self.position}
            \nExperience: {self.experience}
            \nDesired salary: {self.salary}
            \nDesired location: {self.location}
                    """
        else: 
            text = f"""
            Area: {self.area}
            \nSpecialisation: {self.position}
            \nExperience: {self.experience}
            \nLanguage: {self.language}
            \nDesired salary: {self.salary}
            \nDesired location: {self.location}
                    """
        return text
