class Library:
    def __init__(self, listOfBooks):
        self.books= listOfBooks

    def displayAvailableBooks(self):
        print("The books present in library are: ")
        for book in self.books:
            print("  ->" + book)

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname}. Please keep it safe and return it within 30 days")
            self.books.remove(bookname)
            return True 
        else:
            print("Sorry the book is currently not available")
            return False
    
    def returnBook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returning this book. have a good day")


class Student:
    # def __init__(self):
    #     self.bookList= []
    def requestbook(self):
        self.book = input("Enter the name of the book you want to borrow ")
        return self.book

    def returnbook(self):
        self.book = input("Enter the name of the book you want to borrow ")
        return self.book

if __name__== "__main__":
    centralLibrary = Library(["DSA", "OS", "PY", "Database", "Gamer", "free fall"])
    student = Student()

    while(True):
        welcomeMsg= '''
        ******* Welcome to central library *******
        please choose an option 
        1. List all the available books 
        2. Request a book
        3. Add / Return a book
        4. Exit the library
        '''
        print(welcomeMsg)
        a = int(input("Enter your choice: "))

        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestbook())
        elif a==3:
            centralLibrary.returnBook(student.returnbook())
        elif a==4:
            print("Thanks for using this library. have a great day!")
            exit()
        else:
            print("Enter a valid choice ")


