#!/usr/bin/python3

import questionary

class Transaction:
    def main_menu(self):
        questionary.select(
            'Transactions:',
            choices=[
                  'New',
                  'Edit',
                  'Delete'
            ],
            use_shortcuts=True).ask()
    
    def autocomplete(self):
        questionary.autocomplete(
            'Start typing:',
            choices=[
                'Target',
                'Publix',
                'Sam\'s',
                'Kroger',
                'Bed Bath & Beyond',
                'Chick-fil-A',
                'Church',
                'Church\'s Chicken',
                'Amazon'
            ]).ask()

if __name__ == '__main__':
    transaction = Transaction()

    transaction.main_menu()
    transaction.autocomplete()
