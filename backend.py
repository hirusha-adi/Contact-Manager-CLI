import sqlite3

def connect():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()

    # Table name: conlist
    # id : primary key: integer
    # name: text
    # pnumber: text

    cur.execute("CREATE TABLE IF NOT EXISTS conlist (id INTEGER PRIMARY KEY, name text, pnumber text)")
    conn.commit()
    conn.close()


def insert(name, number):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO conlist VALUES (NULL,?,?)",(name, number))

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM conlist")
    rows = cur.fetchall()

    conn.commit()
    conn.close()

    return rows


def delete(id):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM conlist WHERE id=?", (id,))

    conn.commit()
    conn.close()


def search(name="", number=""):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM conlist WHERE name=? OR pnumber=?", (name, number))
    rows = cur.fetchall()

    conn.commit()
    conn.close()

    return rows

# def update(id, name, number):
























