from app.db.session import SessionLocal
from app.db.models import (
    User,
    Book,
    BookPage,
    ReadingProgress,
)
import uuid


def run_test():
    db = SessionLocal()

    try:
        print("Creating user...")
        user = User(
            email=f"test_{uuid.uuid4()}@example.com",
            password_hash="hashedpassword123"
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        print("User ID:", user.id)

        print("Creating book...")
        book = Book(
            user_id=user.id,
            title="Test Book",
            author="Nikhil",
            file_url="s3://fake-path/test.pdf",
            file_hash=str(uuid.uuid4()),
            total_pages=3
        )
        db.add(book)
        db.commit()
        db.refresh(book)

        print("Book ID:", book.id)

        print("Adding pages...")
        for i in range(1, 4):
            page = BookPage(
                book_id=book.id,
                page_number=i,
                content=f"This is page {i}"
            )
            db.add(page)

        db.commit()

        print("Creating reading progress...")
        progress = ReadingProgress(
            user_id=user.id,
            book_id=book.id,
            current_page=2
        )
        db.add(progress)
        db.commit()

        print("\nTesting relationships...")

        db_user = db.query(User).filter(User.id == user.id).first()

        print("User has books:", len(db_user.books))
        print("Book has pages:", len(db_user.books[0].pages))
        print("Current page:", db_user.reading_progress[0].current_page)

        print("\nEverything working correctly 🎉")

    except Exception as e:
        print("Error occurred:", e)
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    run_test()