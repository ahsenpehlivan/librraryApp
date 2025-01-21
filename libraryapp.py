books = []
students = []


def load_books():

    try:
        with open("bookfile.txt", "r", encoding="utf-8") as bookfile:

            for line in bookfile:
                isbn, namebook, author, checked = line.split(",")
                books.append({"ISBN": isbn, "Book Name": namebook, "Author": author, "Checked": checked.strip()})

    except FileNotFoundError:
        with open("bookfile.txt", "x"):
            pass



def load_students():

    try:
        with open("studentfile.txt", "r", encoding="utf-8") as studentfile:

            for line in studentfile:
                student_id, name, surname, *booknames = line.split(" ")

                if len(booknames) > 0:
                    booknames[-1] = booknames[-1].strip()

                students.append({"ID": student_id, "Name": name, "Surname": surname.strip(), "Booksnames": booknames})

    except FileNotFoundError:
        with open("studentfile.txt", "x"):
            pass




def save_books():
    with open('bookfile.txt', 'w', encoding="utf-8") as bookfile:

        for book in books:
            bookfile.write(f"{book['ISBN']},{book['Book Name']},{book['Author']},{book['Checked']}\n")



def save_students():
    with open('studentfile.txt', 'w') as studentfile:

        for student in students:
            studentfile.write(f"{student['ID']} {student['Name']} {student['Surname']} {' '.join(student['Booksnames'])}".strip() + "\n")



def list_all_books():

    for book in books:
        print(f"ISBN: {book['ISBN']}, Book Name: {book['Book Name']}, Author: {book['Author']}, Checked: {book['Checked']}")

    go_back()



def list_books_checked_out():

    for book in books:

        if book["Checked"].strip() == "T":
            print(f"ISBN: {book['ISBN']}, Book Name: {book['Book Name']}, Author: {book['Author']}, Checked: {book['Checked']}")

    go_back()



def newbook():
    isbn_new = int(input("ISBN: ").strip())
    bookname_new = str(input("Book Name: ").strip())
    author_new = str(input("Author: ").strip())
    
    samebook = False

    for book in books:
        if book['ISBN'] == isbn_new:
            samebook = True
            
    if samebook:
        print("This book is already in library")

    else:
        books.append({"ISBN": isbn_new, "Book Name": bookname_new, "Author": author_new, "Checked": "F"})        
        print("Book successfully added!")
        save_books()
        
    go_back()



def deletebook():
    isbn_delete = input("ISBN: ")

    for book in books:

        if book["ISBN"] == isbn_delete:

            if book["Checked"].strip() == "T":
                print("This book is checked out!")

            else:
                books.remove(book)
                print("Book successfully deleted!")
            break
    else:
        print("Book not found!")

    save_books()
    go_back()



def search_isbn_book():

    isbn_search = input("ISBN: ")

    for book in books:

        if book["ISBN"] == isbn_search:
            print(book)
            break

    else:
        print("The book you search for isn't found.")

    go_back()



def search_name_book():

    name_search = str(input("Book Name: "))
    found_books = []

    for book in books:

        if name_search.lower() in book["Book Name"].lower():
            found_books.append(str(book))

    if (len(found_books) > 0):
        print("\n".join(found_books))

    else:
        print("The book you search for isn't found.")

    go_back()



def check_out():
    found_book = None
    found_student = None

    check_isbn = input("ISBN: ")
    check_student = input("Student ID: ")

    for book in books:

        if book["ISBN"] == check_isbn:

            if book["Checked"] == "F":
                found_book = book
                break

            else:
                print("Book is already checked out!")

                go_back()

    else:
        print("Book not found!")
        go_back()

    for student in students:

        if student["ID"] == check_student:
            found_student = student
            break

    if found_student:
        found_student["Booksnames"].append(found_book["ISBN"].strip())
        found_book["Checked"] = "T"

        print("Book checked out successfully!")
        save_students()

    else:
        print("Student not found!")

    go_back()



def list_students():
    with open("studentfile.txt", "r") as studentfile:

        for line in studentfile:
            id_print, name_print, surname_print, *booknames_print = line.split()

            bookmatching = []
            if booknames_print:

                for everybook in booknames_print:

                    for book in books:

                        if everybook == book["ISBN"]:
                            bookmatching.append(book["ISBN"])
                            bookmatching.append(book["Book Name"])

            print(id_print, name_print, surname_print, bookmatching)

    go_back()



def go_back():
    input("Press Enter to go back to the menu...")
    menu()


def exit():
    save_books()
    save_students()
    print("Exiting the library system..")


def menu():
    print("\t \t \t MENU")
    print("1 - List all the books in the library")
    print("2 - List all the books that are checked out")
    print("3 - Add a new book")
    print("4 - Delete a book")
    print("5 - Search a book by ISBN number")
    print("6 - Search a book by name")
    print("7 - Check out a book to a student")
    print("8 - List all the students")
    print("0 - EXIT")
    selection = int(input("Enter the operate number (0-8): "))
    if selection == 0:
        exit()
    elif selection == 1:
        list_all_books()
    elif selection == 2:
        list_books_checked_out()
    elif selection == 3:
        newbook()
    elif selection == 4:
        deletebook()
    elif selection == 5:
        search_isbn_book()
    elif selection == 6:
        search_name_book()
    elif selection == 7:
        check_out()
    elif selection == 8:
        list_students()
    else:
        print("Please enter a variable that between 0 and 8")
        menu()



load_books()
load_students()
menu()