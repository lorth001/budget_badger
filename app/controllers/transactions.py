from app.database import session
from app.models import Transaction


def get_transaction(id):
    transaction = Transaction.query.get(id)
    return transaction

def add_transaction(cat_id, card_id, merch_id, date, amnt):
    transaction = Transaction(category=cat_id, card=card_id, merchant=merch_id, date=date, amount=amnt)
    session.add(transaction)
    session.commit()
    return transaction.id
