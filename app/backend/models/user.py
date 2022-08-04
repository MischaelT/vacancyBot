class User():

    """
    Class represents user model
    """

    def __init__(self, user_id, is_registered, experience, location, salary, area='area', specialisation='specialisation', language = 'English') -> None:

        self.user_id = user_id
        self.is_registered = is_registered
        self.area = area
        self.specialisation = specialisation
        self.experience = experience
        self.language = language
        self.location = location
        self.salary = salary

    def to_print(self):

        if self.area == 'management':

            text = f"""
                                Area: {self.area}\n
                        Specialisation: {self.specialisation}\n
                        Experience: {self.experience}\n
                        Desired salary: {self.salary}\n
                        Desired location: {self.location}
                    """
        else: 
            text = f"""
                                Area: {self.area}\n
                        Specialisation: {self.specialisation}\n
                        Experience: {self.experience}\n
                        Language: {self.language}\n
                        Desired salary: {self.salary}\n
                        Desired location: {self.location}
                    """
        return text
