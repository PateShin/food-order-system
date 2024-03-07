import sqlite3

def submit_pick_order(data):
    conn = sqlite3.connect('data/Detail.db')
    c = conn.cursor()
    c.execute("""INSERT INTO pick VALUES(:entnme, :entphn, :entfnum1, :entfnum2, 
                :entfnum3, :entfnum4, :entfnum5, :entfnum6, :entfnum7, :entfnum8, 
                :entfnum9, :entfnum10, :entfnum11, :entfnum12, :TotalCost, :tem1, 
                :tem2, :tem3, :tem4, :tem5, :tem6, :tem7, :tem8, :tem9, :tem10, 
                :tem11, :tem12)""", data)
    conn.commit()
    conn.close()

def submit_delivery_order(data):
    conn = sqlite3.connect('data/Detail.db')
    c = conn.cursor()
    c.execute("""INSERT INTO delivery VALUES(:entnme, :entphn, :entadr, :entfnum1, 
                :entfnum2, :entfnum3, :entfnum4, :entfnum5, :entfnum6, :entfnum7, 
                :entfnum8, :entfnum9, :entfnum10, :entfnum11, :entfnum12, :TotalCost, 
                :exdel, :tem1, :tem2, :tem3, :tem4, :tem5, :tem6, :tem7, :tem8, :tem9, 
                :tem10, :tem11, :tem12)""", data)
    conn.commit()
    conn.close()
