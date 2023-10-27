import re


class Professor:
    def __init__(self, name, pattern, email):
        self.name = name
        self.pattern = pattern
        self.email = email

    def match(self, message):
        return bool(re.findall(self.pattern, message))
