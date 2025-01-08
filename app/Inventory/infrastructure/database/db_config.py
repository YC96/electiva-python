from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from decouple import config

load_dotenv()

SQLALCHEMY_DATABASE_URL = 'postgresql://%(db_user)s:%(db_passwd)s@%(db_host)s:%(db_port)s/%(db_name)s?client_encoding=utf8' % {
    "db_user": config("POSTGRES_USER"),
    "db_passwd": config("POSTGRES_PASSWORD"),
    "db_host": config("POSTGRES_HOST"),
    "db_port": config("POSTGRES_PORT"),
    "db_name": config("POSTGRES_DB"),
}

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Proporciona una sesión de base de datos para cada solicitud.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_connection():
    """
    Prueba la conexión con la base de datos.
    """
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return result.scalar()
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

if test_connection() == 1:
    print("Connection successful!")
else:
    print("Connection failed.")
