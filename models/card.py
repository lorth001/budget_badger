#!/usr/bin/python3

class Card:
    def __init__(self, card_id, card_name):
        self.card_id = card_id
        self.card_name = card_name

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, c_id):
        if not c_id:
            raise ValueError('Card ID cannot be NULL')
        self._card_id = int(c_id)

    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, c_name):
        if not c_name:
            raise ValueError('Card name cannot be NULL')
        self._card_name = c_name

if __name__ == '__main__':
    card = Card(1, 'AMEX')
    print(card.card_id)
    print(card.card_name)
