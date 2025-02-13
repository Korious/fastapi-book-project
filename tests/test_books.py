from tests import client


def test_get_all_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_single_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"


def test_create_book():
    new_book = {
        "id": 4,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "publication_year": 1997,
        "genre": "Fantasy",
    }
    response = client.post("/books/", json=new_book)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 4
    assert data["title"] == "Harry Potter and the Sorcerer's Stone"


def test_update_book():
    updated_book = {
        "id": 1,
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put("/books/1", json=updated_book)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit: An Unexpected Journey"


def test_delete_book():
    response = client.delete("/books/3")
    assert response.status_code == 204

    response = client.get("/books/3")
    assert response.status_code == 404

#Test: if get_book_by_id is valid
def test_get_book_by_id():
    response = client.get("/books/2")
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
         pytest
======================= test session starts =======================
platform win32 -- Python 3.11.2, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\DELL\Documents\Code\fastapi-book-project
plugins: anyio-4.8.0
collected 6 items                                                  

tests\test_books.py .....F                                   [100%]

============================ FAILURES =============================
_______________________ test_get_book_by_id _______________________

    def test_get_book_by_id():
        response = client.get("/books/2")
        assert response.status_code == 200
>       assert response.json() == {
            "id": 2,
            "title": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
            "publication_year": 1954,
            "genre": "FANTASY",
        }
E       AssertionError: assert {'author': 'J...r': 1954, ...} == {'a
uthor': 'J...r': 1954, ...}
E         
E         Omitting 4 identical items, use -vv to show
E         Differing items:
E         {'genre': 'Fantasy'} != {'genre': 'FANTASY'}
E         Use -v to get more diff

tests\test_books.py:58: AssertionError
===================== short test summary info =====================
FAILED tests/test_books.py::test_get_book_by_id - AssertionError: as
sert {'author': 'J...r': 1954, ...} == {'auth...
================== 1 failed, 5 passed in 15.39s ===================
PS C:\Users\DELL\Documents\Code\fastapi-book-project>
    }

#Test: if get_book_by_id is not valid
response = client.get("/books/999")
assert response.status_code == 404
assert response.json() == {"detail":"Book not found"}