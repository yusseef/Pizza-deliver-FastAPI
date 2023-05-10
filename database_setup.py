from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Engine = create_engine('postgresql://postgres:admin@localhost/pizza_delivery', echo = True)

Base = declarative_base() #Declarative classes are those that define their table schema using a set of class variables, rather than actual SQL.

Session = sessionmaker() #This is a module that provides a way to create a session factory which can be used to create new sessions with a given database connection