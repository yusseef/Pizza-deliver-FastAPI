from database_setup import Base, Session
from sqlalchemy import Column, Integer, String, Text, Boolean,

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(70), unique=True)
    password = Column(Text(255), nullable = True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User: {self.username} // {self.email}"
    
