from datetime import date

class User:
    def __init__(self, name, birth = date.today(), nick_name = "", email = ""):
        self.name = name
        self.birth = birth
        self.nick_name = nick_name
        self.email = email

