from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from app.database import Base, engine


class Institution(Base):
    __tablename__ = 'institutions'

    id      = Column(Integer, primary_key=True)
    name    = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return (f'<Institution(id: {self.id}, name: "{self.name}")>')


class Card(Base):
    __tablename__ = 'cards'

    id              = Column(Integer, primary_key=True)
    institution     = Column(Integer, ForeignKey(Institution.id), nullable=False)
    user            = Column(Integer, ForeignKey(User.id), nullable=False)
    last_four       = Column(Integer, nullable=False)

    institution     = relationship(Institution, backref=backref('cards', lazy='joined'))
    user            = relationship(User, backref=backref('cards', lazy='joined'))
    __table_args__  = (UniqueConstraint('institution', 'user', 'last_four'),)

    def __repr__(self):
        return (f'<Card(id: {self.id}, institution: "{self.institution}",'
                f' user: {self.user}, last_four: {self.last_four})>')


class User(Base):
    __tablename__ = 'users'

    id          = Column(Integer, primary_key=True)
    first_name  = Column(String, nullable=False)
    last_name   = Column(String, nullable=False)

    def __repr__(self):
        return (f'<User(id: {self.id}, first_name: "{self.first_name}",'
                f' last_name: "{self.last_name}")>')


class Category(Base):
    __tablename__ = 'categories'

    id      = Column(Integer, primary_key=True)
    name    = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f'<Category(id: {self.id}, name: "{self.name}")>'


class Merchant(Base):
    __tablename__ = 'merchants'

    id      = Column(Integer, primary_key=True)
    name    = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return (f'<Merchant(id: {self.id}, name: "{self.name}")>')


class Transaction(Base):
    __tablename__ = 'transactions'

    id          = Column(Integer, primary_key=True)
    category    = Column(Integer, ForeignKey(Category.id), nullable=False)
    card        = Column(Integer, ForeignKey(Card.id), nullable=False)
    merchant    = Column(Integer, ForeignKey(Merchant.id), nullable=False)
    _date       = Column(DateTime, nullable=False)
    _amount     = Column(Integer, nullable=False)

    category    = relationship(Category, backref=backref('transactions', lazy='joined'))
    card        = relationship(Card, backref=backref('transactions', lazy='joined'))
    merchant    = relationship(Merchant, backref=backref('transactions', lazy='joined'))

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
        return (f'<Transaction(id: {self.id}, category: {self.category},'
                f' card: {self.card}, merchant: {self.merchant},'
                f' date: {self.date}, amount: {self.amount})>')


class Mapper(Base):
    __tablename__ = 'mappers'
    
    id              = Column(Integer, primary_key=True)
    institution     = Column(Integer, nullable=False)
    category        = Column(Integer, nullable=False)
    merchant        = Column(Integer, nullable=False)
    inst_merch_id   = Column(String, nullable=False)
    name            = Column(String, nullable=False)

    institution     = relationship(Institution, backref=backref('mappers', lazy='joined'))
    category        = relationship(Category, backref=backref('mappers', lazy='joined'))
    merchant        = relationship(Merchant, backref=backref('mappers', lazy='joined'))
    __table_args__  = (UniqueConstraint('institution', 'name'),)

    def __repr__(self):
        return (f'<Mapper(id: {self.id}, institution: {self.institution},'
                f' category: {self.category}, merchant: {self.merchant},'
                f' inst_merch_id: "{self.inst_merch_id}", name: "{self.name}")>')


# Generate database schema
Base.metadata.create_all(bind=engine)
