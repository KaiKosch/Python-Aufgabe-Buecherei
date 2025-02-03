from Book import *
from Person import *

class Member(Person):
    def __init__(self, name:str, email:str, member_id:int):
        super().__init__(name, email)
        self._member_id = member_id
        self._borrowed_books = []

    def get_member_id(self)->int:
        return self._member_id
    
    def get_borrowed_books(self)->list:
        return self._borrowed_books
    
    def show_borrowed_books(self)->str:
        output = f"--- Buecher von {self.get_name()} ---\n"
        for book in self._borrowed_books:
            output += book.__repr__() + "\n"

        return output
    
    def add_borrowed_book(self, book:Book)->bool:
        self._borrowed_books.append(book)
    
    def __str__(self)->str:
        return f"Name: {self._name}\nEmail: {self._email}\nMember-Id: {self._member_id}\n"
    
    def __repr__(self)->str:
        return self._name