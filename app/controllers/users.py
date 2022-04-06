from app.database import session
from app.models import User


def get_user(id):
    user = User.query.get(id)
    return user

def add_user(f_name, l_name):
    user = User(first_name=f_name, last_name=l_name)
    session.add(user)
    session.commit()
    return user.id
