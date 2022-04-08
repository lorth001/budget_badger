from app.database import session
from app.models import Merchant


def get_merchant(id):
    merchant = Merchant.query.get(id)
    return merchant

def add_merchant(name):
    merchant = Merchant(name=name)
    session.add(merchant)
    session.commit()
    return merchant.id
