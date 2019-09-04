import csv
from data import session_factory

from data.models.books import Book
from data.models.borrowings import Borrowing
from data.models.branches import Branch
from data.models.clients import Client

def import_if_empty():
    import_branches()
    import_books()
    import_borrowings()
    import_clients()


def import_branches():
    session = session_factory.create_session()
    if session.query(Branch).count() > 0:
        return

    branch = Branch()
    branch.street = "6802 Grim Hill" 
    branch.district = "Old Town"
    branch.phone_no = 652796716
    session.add(branch)

    branch = Branch()
    branch.street = "094 Russell Trail"
    branch.district = "New City"
    branch.phone_no = 667139351
    session.add(branch) 

    branch = Branch()
    branch.street = "8 Valley Edge Court"
    branch.district = "Greenfield"
    branch.phone_no = 729844653
    session.add(branch)

    branch = Branch()
    branch.street = "6 Cherokee Park"
    branch.district = "Black Yard"
    branch.phone_no = 683996375
    session.add(branch) 

    session.commit()

def import_books():
    session = session_factory.create_session()
    if session.query(Book).count() > 0:
        return

    with open("books.csv", newline="") as f:
        f_reader = csv.reader(f, delimiter=";")
        for row in f_reader:
            book = Book()
            book.author = row[0]
            book.title = row[1]
            book.year = row[2]
            book.branch_id = row[3]
            session.add(book)
        session.commit()


def import_clients():
    session = session_factory.create_session()
    if session.query(Client).count() > 0:
        return

    with open("clients.csv", newline="") as f:
        f_reader = csv.reader(f, delimiter=";")
        for row in f_reader:
            client = Client()
            client.first_name = row[0]
            client.last_name = row[1]
            client.email = row[2]
            session.add(client)
    session.commit()


def import_borrowings():
    pass
    

