import sqlite3
import webbrowser

conn = sqlite3.connect(':memory:') #Store in memory database
#conn = sqlite3.connect('favs.db') #To store on a database

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS favorites (title TEXT, url TEXT)''')

def add_fav(title, url):
    c.execute('''INSERT INTO favorites (title, url) VALUES(?, ?)''', (title, url))
    conn.commit()

def remove_fav(title):
    c.execute('''DELETE FROM favorites WHERE title=?''', (title,))
    conn.commit()

def get_favs():
    c.execute('''SELECT * FROM favorites''')
    return c.fetchall()


def get_fav(title):
    c.execute('''SELECT * FROM favorites WHERE title=?''', (title,))
    return c.fetchone()

while True:
    response = input('To visit a favorite press v, to view a list type ls, to add a new list type add, to remove from '
                     'the list type rm, if you like to quit press q: ')
    if response == 'v':
        shortcut = input("What is the shortcut?: ")
        record = get_fav(shortcut)
        print(record)
        try:
            webbrowser.open(record[1])
        except:
            print("cannot open, shortcut does not exist")
    elif response == 'ls':
        print(get_favs())
    elif response == 'add':
        destination = input('Where do you want this shortcut to go?: ')
        shortcut = input('What is the shortcut?: ')
        add_fav(shortcut, destination)
    elif response == 'rm':
        shortcut = input('What is the shortcut?: ')
        remove_fav(shortcut)
    elif response == 'q':
        break


