import sqlite3

# Create a mock database
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE users (username TEXT, password TEXT)')
c.execute("INSERT INTO users VALUES ('admin', 'password123')")
conn.commit()

def sql_injection_attack(injection):
    query = f"SELECT * FROM users WHERE username = '{injection}'"
    c.execute(query)
    return c.fetchall()

if __name__ == "__main__":
    user_input = input("Enter username: ")
    results = sql_injection_attack(user_input)
    if results:
        print(f"User found: {results}")
    else:
        print("No user found.")