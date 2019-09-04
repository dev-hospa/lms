import sqlalchemy as sa
from data import session_factory
from services import data_service
import import_data


def main():
    setup_db()

    run = True
    while run:
        task = input("""
        [B] for borrowing a book
        [R] for returning a book
        [H] for seeing history of borrowings
        [Q] QUIT
        """).upper()

        if task == "B":
            borrow_book()
        elif task == "R":
            return_book()
        elif task == "H":
            client_history()
        elif task == "Q":
            run = False
        else:
            print("wrong command")



    # find_book_by_title("engineer dot-com initiatives")
    # print()
    # find_book_by_author("Daisi Durtnell")
    # print()
    # borrow_book()
    # print()
    # my_history()
    # print()
    # return_book()

    
def setup_db():
    global client
    session_factory.global_init()       # 1. initialize the connection / engine
    session_factory.create_tables()     # 2. create the tables
    import_data.import_if_empty()       # 3. import data
    client = data_service.login_client()# 4. choose client

    
def find_book_by_title(title):
    found_books = data_service.books_by_title(title)
    if found_books:
        for book in found_books:
            print(book)


def find_book_by_author(author):
    found_books = data_service.books_by_author(author)

    if found_books:
        print(f"Books by {author}: ")
        for idx, book in enumerate(found_books, start=1):
            print(f"{idx}: {book.title}. Branch: {book.branch}. {book.available}")
        return found_books

    return None
    

def borrow_book():
    author = input("Which author are you interested in? ")
    books = find_book_by_author(author)

    if books:
        choice = input("Which one do you want to borrow? ")
        try:
            choice = int(choice) - 1
        except:
            print("wrong command")
            return

        if (choice >= 0 and choice < len(books)):
            if not data_service.is_free(books[choice].id):
                print("this book is already borrowed, choose another one")
                return
            
            borrowing = data_service.create_borrowing(books[choice].id, client.id)
            print(data_service.borrowing_details(borrowing))
        else:
            return

    return


def return_book():
    # print my borrowings which are still opened
    borrowings = data_service.opened_borrowings(client.id)
    for borrowing in borrowings:
        print(borrowing)
    # choose which book you want to return
    idx = input("which borrowing (ID) do you wish to close? ")
    try:
        idx = int(idx)
    except:
        print("wrong command")
        return
    # change book.available to free
    if idx in [borrowing.id for borrowing in borrowings]:
        data_service.close_borrowing(idx)
    print("wrong ID")
    


def client_history():
    client_id = client.id
    list_of_borrowings = data_service.list_of_borrowing(client_id)

    if list_of_borrowings:
        for item in list_of_borrowings:
            print(item)

    return




if __name__ == '__main__':
    main()