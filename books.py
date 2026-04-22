from fastapi import FastAPI

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