import sqlite3
import csv
from tkinter import END

def delivery(txtReceipt1):
    conn = sqlite3.connect('data/Detail.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM delivery")
    records = c.fetchall()
    txtReceipt1.delete("1.0", END)
    
    # Read pasta names from the CSV file
    pasta_names = []
    with open('data/pasta_name.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            pasta_names.append(row[0])
    
    for record in records:
        txtReceipt1.insert(END, "ID:"+str(record[-1])+ "\n" +"Name: "+str(record[0])+ "      " + "Phone: "+str(record[1]) + "\n" +"Address: " +str(record[2])+"\n")
        txtReceipt1.insert(END, "----------------------------------------------" + "\n")
        
        # Adjusted indices to match the given record structure
        for i, pasta_name in enumerate(pasta_names, start=3):  # Starting from 3 to match the given record structure
            qty_index = i
            price_index = i + 14  # Adjusting to start from 16 for price indices, as per the given structure
            if record[qty_index] > 0:
                txtReceipt1.insert(END, f"{pasta_name}\t\t\t\t{record[qty_index]}x {record[price_index]}\n")
                
        txtReceipt1.insert(END, "Total Cost:" + "\t\t\t\t" + str(record[15]) + "\n\n\n")
    
    conn.close()
