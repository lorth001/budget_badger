from app.database import session
from app.models import Mapper


def get_mapper(id):
    mapper = Mapper.query.get(id)
    return mapper

def add_mapper(inst_id, cat_id, merch_id, inst_merch_id, name):
    mapper = Mapper(institution=inst_id, category=cat_id, merchant=merch_id, 
                    inst_merch_id=inst_merch_id, name=name)
    session.add(mapper)
    session.commit()
    return mapper.id
