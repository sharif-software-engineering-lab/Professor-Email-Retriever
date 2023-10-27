import re


class Professor:
    def __init__(self, name, pattern, email):
        self.name = name
        self.pattern = pattern
        self.email = email

    def match(self, message):
        return bool(re.match(self.pattern, message))
    
    def __str__(self) -> str:
        return f"{self.name}: {self.email}"
