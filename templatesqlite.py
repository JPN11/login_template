import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('accounts.db')
cursor = conn.cursor()

# Create a table for storing user accounts
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Function to create a new account
def create_account(username, password):
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print("Account created successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")

# Function to sign in
def sign_in(username, password):
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    account = cursor.fetchone()
    if account:
        print("Sign-in successful!")
    else:
        print("Invalid username or password.")

# Example usage
prompt = int(input("""1> Create account
2> Sign in\n"""))

if prompt == 1:
    username = input("Enter username: ")
    password = input("Enter password: ")
    create_account(username, password)
elif prompt == 2:
    signname = input("Enter username: ")
    signword = input("Enter password: ")
    sign_in(signname, signword)

# Close the connection
conn.close()
