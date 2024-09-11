from __init__ import CONN, CURSOR


def create_database_table():
    sql = """
        CREATE TABLE IF NOT EXISTS bank_users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owners_name TEXT NOT NULL,
            location TEXT NOT NULL,
            account_number INTEGER NOT NULL
        )
    """
    CURSOR.execute(sql)
    CONN.commit()


class BankApplication:
    def __init__(self, owners_name, location, account_number):
        self.owners_name = owners_name
        self.location = location
        self.account_number = account_number

    def __str__(self):
        return f"Account for {self.owners_name} has been created successfully, and account number is {self.account_number}."


def main():
    create_database_table()

    print("Welcome to the Bank of Moringa Application.")
    while True:
        print("Menu options")
        print("1. Create an account")
        print("2. Exit")

        menu_options = input("Choose from menu options: ")
        if menu_options == "1":
            owners_name = input("Enter your fullname: ")
            location = input("Enter your location: ")
            account_number = input("Enter account number: ")

            sql = """
                SELECT * FROM bank_users
                WHERE account_number = ?
            """
            db_cursor = CURSOR.execute(sql, (account_number,))
            results = db_cursor.fetchone()

            if results:
                print("Account already exists!!!")
            else:
                sql = """
                    INSERT INTO bank_users (owners_name, location, account_number)
                    VALUES (?, ?, ?)
                """
                CURSOR.execute(sql, (owners_name, location, account_number,))
                CONN.commit()
                print(f"account for {owners_name} has been created successfully. account number is {account_number}")
        elif menu_options == "2":
            break
        else:
            print("Invalid option. Choose correct option")
if __name__ == "__main__":
    main()      


