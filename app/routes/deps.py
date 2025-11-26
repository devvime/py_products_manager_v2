from app.database.connection import Session

def get_database_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()