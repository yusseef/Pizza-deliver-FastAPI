from database_setup import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(70), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship("Order", back_populates='user', cascade = "all, delete-orphan")

    def __repr__(self):
        return f"<User: {self.username} // {self.email}"
    
    
class Order(Base):
    STATUSES = [
        ('PENDING', 'pending'),
        ('IN TRANSITION', 'in_transition'),
        ('DELIVERED', 'delivered')
    ]
    SIZES = [
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
    ]

    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=STATUSES), default='PENDING')
    pizza_size = Column(ChoiceType(choices=SIZES), default='SMALL')
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User', back_populates='orders' )

    def __repr__(self):
        return f"<Order {self.id} by {self.user}"