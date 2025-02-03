class Person:
    def __init__(self, name:str, email:str):
        self._name = name
        self._email = email

    def get_name(self)->str:
        return self._name
    
    def get_email(self)->str:
        return self._email