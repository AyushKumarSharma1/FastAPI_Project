from fastapi import FastAPI, Body

app = FastAPI()

BOOK = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Fiction"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction"},
    {"title": "1984", "author": "George Orwell", "category": "Dystopian"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "category": "Romance"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Fiction"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "category": "Fantasy"}
]

@app.get("/books")
async def read_books():
    return BOOK

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    if book_id < len(BOOK):
        return BOOK[book_id-1]
    return {"error": "Book not found"}

@app.get("/books/author/")
async def read_books_by_author(author: str, category: str):
    if category:
        return [book for book in BOOK if book["author"] == author and book["category"] == category]
    return {"error": "Category is required"}

@app.post("/books")
async def create_book(book: dict = Body()):
    BOOK.append(book)
    return {"message": "Book added successfully", "book": book}

@app.put("/books/{book_title}")
async def update_book(book_title: str, updated_book: dict = Body()):
    for i, book in enumerate(BOOK):
        if book["title"].casefold() == book_title.casefold():
            BOOK[i] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}
    return {"error": "Book not found"}

@app.delete("/books/{book_title}")
async def delete_book(book_title: str):
    for i, book in enumerate(BOOK):
        if book["title"].casefold() == book_title.casefold():
            deleted_book = BOOK.pop(i)
            return {"message": "Book deleted successfully", "book": deleted_book}
    return {"error": "Book not found"}
