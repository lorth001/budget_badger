from app.database import session
from app.models import Transaction


def get_transaction(id):
    transaction = Transaction.query.get(id)
    return transaction

def add_transaction(date, amnt, cat_id, u_id, c_id):
    transaction = Transaction(date=date, amount=amnt, category_id=c_id, user_id=u_id, card_id=c_id)
    session.add(transaction)
    session.commit()
    return transaction.id
