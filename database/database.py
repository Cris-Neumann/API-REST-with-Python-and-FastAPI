from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from typing import Generator

db = 'YOUR_DATABASE_NAME'
server = 'YOUR_SERVER_NAME_OR_IP'
engine = create_engine('mssql+pyodbc://@' + server + '/' + db + '?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
