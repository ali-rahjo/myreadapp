from src.db.database import Database

def list_title_by_format_and_reader_title(format_: str, title: str):
    conn = Database
    # list title of a specific book format read by reader of a specific title

    query = """SELECT DISTINCT b.title FROM book b
JOIN my_read m ON b.isbn = m.book_isbn
JOIN reader r ON m.reader_username = r.username
WHERE r.title = 'Dr';

"""

    with conn.cursor() as cursor:
        cursor.execute(query, (title, format_))
        list = cursor.fetchall()
        return list
    