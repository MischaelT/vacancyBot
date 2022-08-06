from backend.data.db.choices import DEVELOPMENT, MANAGEMENT, TEST

from frontend.data.consts import (AREAS_LIST, DEVELOPER_OPTIONS,
                                  EXPERIENCES_LIST, LANGUAGE_LIST,
                                  MANAGEMENT_OPTIONS, QA_OPTIONS)


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
            specialisation = MANAGEMENT_OPTIONS[self.position]
        elif self.area == DEVELOPMENT:
            specialisation = DEVELOPER_OPTIONS[self.position]
        elif self.area == TEST:
            specialisation = QA_OPTIONS[self.position]
        elif self.area == MANAGEMENT:
            specialisation = QA_OPTIONS[self.position]

        if self.area == MANAGEMENT:
            text = f"""
            Area: {AREAS_LIST[self.area]}
            \nSpecialisation: {specialisation}
            \nExperience: {EXPERIENCES_LIST[self.experience]}
            \nDesired salary: {self.salary}
            \nDesired location: {self.location}
                    """
        else:
            text = f"""
            Area: {AREAS_LIST[self.area]}
            \nSpecialisation: {specialisation}
            \nExperience: {EXPERIENCES_LIST[self.experience]}
            \nLanguage: {LANGUAGE_LIST[self.language]}
            \nDesired salary: {self.salary}
            \nDesired location: {self.location}
                    """

        return text
