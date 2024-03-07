import sqlite3

conn = sqlite3.connect('data/Detail.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS delivery (
    entnme TEXT,
    entphn TEXT,
    entadr TEXT,
    entfnum1 INTEGER,
    entfnum2 INTEGER,
    entfnum3 INTEGER,
    entfnum4 INTEGER,
    entfnum5 INTEGER,
    entfnum6 INTEGER,
    entfnum7 INTEGER,
    entfnum8 INTEGER,
    entfnum9 INTEGER,
    entfnum10 INTEGER,
    entfnum11 INTEGER,
    entfnum12 INTEGER,
    TotalCost REAL,
    exdel TEXT,
    tem1 TEXT,
    tem2 TEXT,
    tem3 TEXT,
    tem4 TEXT,
    tem5 TEXT,
    tem6 TEXT,
    tem7 TEXT,
    tem8 TEXT,
    tem9 TEXT,
    tem10 TEXT,
    tem11 TEXT,
    tem12 TEXT
)
''')

conn.commit()
conn.close()
