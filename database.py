from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

USERNAME = 'root'
PASSWORD = ''
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = 'pizza_delivery'

URL_DATABASE = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(URL_DATABASE, echo=True)

Base = declarative_base()

Session = sessionmaker()