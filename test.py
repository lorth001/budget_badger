from app.controllers import cards, users, categories, transactions


'''
USER
'''
# add a user and return the ID
user = users.add_user('Molly', 'Orth')

# get a user with ID
print(users.get_user(user))

'''
CATEGORY
'''
# add a category and return the ID
category = categories.add_category('Groceries')

# get a category with ID
print(categories.get_category(category))

'''
CARD
'''
# add a card and return the ID
card = cards.add_card('Chase', 7777, user)

# get a card with ID
print(cards.get_card(card))

'''
TRANSACTION
'''
# add a transaction and return the ID
transaction = transactions.add_transaction('2022-04-06', 7.52, 1, 1, 1)

# get a transaction with ID
print(transactions.get_transaction(transaction))
