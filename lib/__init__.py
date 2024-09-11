import sqlite3

CONN = sqlite3.connect("bank_of_moringa.db")
CURSOR = CONN.cursor()