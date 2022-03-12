class User():

    """
    Class represents user model
    """

    def __init__(self, user_id, is_registered, experience, city, language, salary) -> None:

        self.user_id = user_id
        self.is_registered = is_registered
        self.experience = experience
        self.language = language
        self.city = city
        self.salary = salary

    def to_print(self):

        text = f"""
                    Experience: {self.experience}\n
                    Language: {self.language}\n
                    Desired salary: {self.salary}\n
                    Desired city: {self.city}
                """

        return text
