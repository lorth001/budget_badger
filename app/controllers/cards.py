from app.database import session
from app.models import Card


def get_card(id):
    card = Card.query.get(id)
    return card

def add_card(inst, user_id, last_four):
    card = Card(institution=inst, user=user_id, last_four=last_four)
    session.add(card)
    session.commit()
    return card.id
