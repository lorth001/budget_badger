from app.database import session
from app.models import Card


def get_card(id):
    card = Card.query.get(id)
    return card

def add_card(inst, l_four, u_id):
    card = Card(institution=inst, last_four=l_four, user_id=u_id)
    session.add(card)
    session.commit()
    return card.id
