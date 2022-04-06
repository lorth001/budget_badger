from app.controllers import cards, users


user = users.add_user('Molly', 'Orth')
card = cards.add_card('Chase', 7777, user)

print(card)

print(cards.get_card(card))
