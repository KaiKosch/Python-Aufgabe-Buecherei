class Book:
    def __init__(self, title:str, author:str, isbn:int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def getTitle(self)->str:
        return self.title
    
    def getAuthor(self)->str:
        return self.author
    
    def getIsbn(self)->int:
        return self.isbn
    
    def getAvailability(self)->bool:
        return self.available
    
    def changeAvailability(self)->bool:
        if self.available:
            self.available = False
            return True
        else:
            self.available = True
            return True
        
    def __str__(self)->str:
        return f"Titel: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nVerfuegbarkeit: {self.available}\n"
    
    def __repr__(self)->str:
        return self.title
