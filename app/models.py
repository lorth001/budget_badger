from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, backref
from datetime import datetime

engine = create_engine('sqlite:///budget-badger.db')
Model = declarative_base(name='Model')

class User(Model):
    __tablename__ = 'users'

    id          = Column(Integer, primary_key=True)
    first_name  = Column(String, nullable=False)
    last_name   = Column(String, nullable=False)

    def __repr__(self):
        return (f'<User(id: {self.id}, first_name: "{self.first_name}",'
                f' last_name: "{self.last_name}")>')


class Category(Model):
    __tablename__ = 'categories'

    id      = Column(Integer, primary_key=True)
    name    = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f'<Category(id: {self.id}, name: "{self.name}")>'


class Card(Model):
    __tablename__ = 'cards'

    id      = Column(Integer, primary_key=True)
    name    = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f'<Card(id: {self.id}, name: "{self.name}")>'


class Transaction(Model):
    __tablename__ = 'transactions'

    id          = Column(Integer, primary_key=True)
    _date       = Column(DateTime, nullable=False)
    _amount     = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    user_id     = Column(Integer, ForeignKey(User.id), nullable=False)
    card_id     = Column(Integer, ForeignKey(Card.id), nullable=False)

    category    = relationship(Category, backref=backref('transactions', lazy='joined'))
    user        = relationship(User, backref=backref('transactions', lazy='joined'))
    card        = relationship(Card, backref=backref('transactions', lazy='joined'))

    @hybrid_property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = datetime.strptime(date, '%Y-%m-%d')

    @hybrid_property
    def amount(self):
        return self._amount / 100

    @amount.setter
    def amount(self, amount):
        self._amount = amount * 100

    def __repr__(self):
        return (f'<Transaction(id: {self.id}, date: {self.date},'
                f' amount: {self.amount}, category_id: {self.category_id},'
                f' user_id: {self.user_id}, card_id: {self.card_id})>')


Model.metadata.create_all(bind=engine)
