from Member import *

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def addBook(self, book:Book)->bool:
        if isinstance(book, Book):
            self.books.append(book)
            return True
        else:
            return False
        
    def delBook(self, title:str)->bool:
        for book in self.books:
            if book.getTitle() == title:
                self.books.remove(book)
                return True
            
        return False
    
    def showBooks(self)->str:
        output = "\t --- Buecher ---\n"
        for book in self.books:
            output += str(book) + "\n"

        return output
    
    def borrowBook(self, title:str, member_id:int)->bool:
        for book in self.books:
            if book.getTitle() == title:
                if book.getAvailability():
                    book.changeAvailability()
                    self.members[member_id - 1].add_borrowed_book(book)
                    return True
                else:
                    print("Das Buch ist nicht verfügbar.")
                    return False
            
        print("Das Buch gibt es nicht in der Bibliothek.")
        return False
    
    def returnBook(self, title:str, member_id:int)->bool:
        for book in self.members[member_id - 1].get_borrowed_books():
            if book.getTitle() == title:
                self.members[member_id - 1].get_borrowed_books().remove(book)
                book.changeAvailability()
                return True
            else:
                print("Das Buch wurde nicht vom Mitglied ausgeliehen.")
                return False
    
    def addMember(self, member:Member)->bool:
        if isinstance(member, Member):
            self.members.append(member)
            return True
        else:
            return False
        
    def delMember(self, name:str)->bool:
        for member in self.members:
            if member.get_name() == name:
                self.members.remove(member)
                return True
            
        return False
    
    def showMembers(self)->str:
        output = "\t--- Mitglieder ---\n"
        for member in self.members:
            output += str(member) + "\n"

        return output
    
    def writeJSON(self):
        json = '{\n' + '\t"Books": {\n'

        # Bucheinträge dem String hinzufügen
        for i in range(0, len(self.books)):
            json += f'\t\t"Buch{i+1}":' + ' {\n'
            json += f'\t\t\t"Titel": "{self.books[i].getTitle()}",\n'
            json += f'\t\t\t"Author": "{self.books[i].getAuthor()}",\n'
            json += f'\t\t\t"ISBN": "{self.books[i].getIsbn()}"\n'
            json += '\t\t}'
            if i < len(self.books) - 1:
                json += ',\n\n'
            else:
                json += '\n'

        json += '\t},\n\n' + '\t"Members": {\n'

        # Membereintrräge dem String hinzufügen
        for i in range(0, len(self.members)):
            json += f'\t\t"Member{i+1}":' + ' {\n'
            json += f'\t\t\t"Name": "{self.members[i].get_name()}",\n'
            json += f'\t\t\t"Email": "{self.members[i].get_email()}",\n'
            json += f'\t\t\t"Member-Id": {self.members[i].get_member_id()}\n'
            json += '\t\t}'
            if i < len(self.members) - 1:
                json += ',\n\n'
            else:
                json += '\n'

        json += '\t}\n}'

        # In Textdatei schreiben
        with open('ausgabe.json', 'w') as datei:
            datei.write(json)

    def writeXML(self):
        xml = '<?xml version="1.0" encoding="utf-8" ?>\n\n'
        xml += '<Library>\n\t<Books/>\n\n\t<Members>\n'

        # Member in String schreiben
        for member in self.members:
            xml += '\t\t<Member>\n'
            xml += f'\t\t\t<Name>{member.get_name()}</Name>\n'
            xml += '\t\t\t<Borrowed>\n'

            # Books in String unter Member schreiben
            for book in member.get_borrowed_books():
                xml += '\t\t\t\t<Book>\n'
                xml += f'\t\t\t\t\t<Title>{book.getTitle()}</Title>\n'
                xml += '\t\t\t\t</Book>\n'

            xml += '\t\t\t</Borrowed>\n'
            xml += '\t\t</Member>\n\n'

        xml += '\t</Members>\n'
        xml += '</Libraray>'

        # In Textdatei schreiben
        with open('ausgabe.xml', 'w') as datei:
            datei.write(xml)