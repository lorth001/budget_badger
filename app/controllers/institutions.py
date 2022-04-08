from app.database import session
from app.models import Institution


def get_institution(id):
    institution = Institution.query.get(id)
    return institution

def add_institution(name):
    institution = Institution(name=name)
    session.add(institution)
    session.commit()
    return institution.id
