#!/usr/bin/env bash

# Creates tables in sqlite

: '
USERS:
	user_id			INTEGER NOT NULL	PRIMARY KEY
	user_first_name	TEXT	NOT NULL
	user_last_name	TEXT	NOT NULL
'
sqlite3 budget-badger.db "CREATE TABLE users (user_id INTEGER PRIMARY KEY NOT NULL, user_first_name TEXT NOT NULL, user_last_name TEXT NOT NULL);" && echo "Success: table users created"

: '
CATEGORIES:
	category_id		INTEGER	NOT NULL	PRIMARY KEY
	category_name	TEXT	NOT NULL	UNIQUE
'
sqlite3 budget-badger.db "CREATE TABLE categories (category_id INTEGER PRIMARY KEY NOT NULL, category_name TEXT NOT NULL UNIQUE);" && echo "Success: table categories created"

: '
CARDS:
	card_id		INTEGER	NOT NULL	PRIMARY KEY
	card_name	TEXT	NOT NULL	UNIQUE
'
sqlite3 budget-badger.db "CREATE TABLE cards (card_id INTEGER PRIMARY KEY NOT NULL, card_name TEXT NOT NULL UNIQUE);" && echo "Success: table cards created"

: '
TRANSACTIONS:
	transaction_id		INTEGER	NOT NULL	PRIMARY KEY
	transaction_date	TEXT	NOT NULL
	transaction_amount	REAL	NOT NULL
	category_id			INTEGER NOT NULL
	user_id				INTEGER NOT NULL
	card_id				INTEGER NOT NULL
	FOREIGN KEY(user_id)		REFERENCES	users(user_id)
	FOREIGN KEY(category_id)	REFERENCES	categories(category_id)
	FOREIGN KEY(card_id)		REFERENCES cards(card_id)
'
sqlite3 budget-badger.db "CREATE TABLE transactions (transaction_id INTEGER PRIMARY KEY NOT NULL, transaction_date TEXT NOT NULL, transaction_amount REAL NOT NULL, category_id INTEGER NOT NULL, user_id INTEGER NOT NULL, card_id INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(user_id), FOREIGN KEY(category_id) REFERENCES categories(category_id), FOREIGN KEY(card_id) REFERENCES cards(card_id));" && echo "Success: table transcations created"

