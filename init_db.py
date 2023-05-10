from database_setup import Engine, Base, Session
from models import User, Order

Base.metadata.create_all(bind = Engine)