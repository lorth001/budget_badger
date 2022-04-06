from app.models import User, Category, Card, Transaction
from app.database import session


new_user = User(first_name='Luke', last_name='Orth')
session.add(new_user)
session.commit()
users = User.query.all()
for user in users:
    print(user)

new_category = Category(name='Groceries')
session.add(new_category)
session.commit()
categories = Category.query.all()
for category in categories:
    print(category)

new_card = Card(institution='AMEX', last_four=6666, user_id=1)
session.add(new_card )
session.commit()
cards = Card.query.all()
for card in cards:
    print(card)

new_transaction = Transaction(date='2022-04-04', amount=700, category_id=1, user_id=1, card_id=1)
session.add(new_transaction)
session.commit()
transactions = Transaction.query.all()
for transaction in transactions:
    print(transaction)
