from models import engine, User, Category, Card, Transaction
from sqlalchemy import event
from sqlalchemy.orm import scoped_session, sessionmaker

session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)

@event.listens_for(engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()

s1 = session()

new_user = User(first_name='Luke', last_name='Orth')
s1.add(new_user)
s1.commit()
users = s1.query(User).all()
for user in users:
    print(user)

new_category = Category(name='Groceries')
s1.add(new_category)
s1.commit()
categories = s1.query(Category).all()
for category in categories:
    print(category)

new_card = Card(name='AMEX')
s1.add(new_card )
s1.commit()
cards = s1.query(Card).all()
for card in cards:
    print(card)

new_transaction = Transaction(date='2022-04-04', amount=700, category_id=1, user_id=1, card_id=1)
s1.add(new_transaction)
s1.commit()
transactions = s1.query(Transaction).all()
for transaction in transactions:
    print(transaction)

s1.close()
