from Library import *

if __name__ == "__main__":
    
    library0 = Library()

    library0.addBook(Book("Harry Potter", "J.K.Rowling", 1234))
    library0.addBook(Book("Tintenherz", "Cornelia Funke", 5678))
    print(library0.showBooks())

    library0.addMember(Member("Annau, Philipp", "PA@conti.de", 1))
    library0.addMember(Member("Kosch, Kai", "kai.ko@mail.de", 2))
    library0.addMember(Member("Tastemir, Celil", "Celil@conti.com", 3))
    print(library0.showMembers())

    library0.borrowBook("Harry Potter", 1)
    print(library0.members[0].show_borrowed_books())
    library0.borrowBook("Tintenherz", 1)
    print(library0.members[0].show_borrowed_books())
    print(library0.showBooks())

    #library0.returnBook("Harry Potter", 1)
    #print(library0.members[0].show_borrowed_books())
    #print(library0.showBooks())

    library0.writeJSON()
    library0.writeXML()