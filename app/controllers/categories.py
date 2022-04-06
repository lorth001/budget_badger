from app.database import session
from app.models import Category


def get_category(id):
    category = Category.query.get(id)
    return category

def add_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    return category.id
