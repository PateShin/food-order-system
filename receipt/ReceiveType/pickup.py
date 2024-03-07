import sqlite3
from tkinter import END

import csv

def pickup(txtReceipt):
    conn = sqlite3.connect('data/Detail.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM pick")
    records = c.fetchall()
    txtReceipt.delete("1.0", END)
    
    # Read pasta names from the CSV file
    pasta_names = []
    with open('data/pasta_name.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            pasta_names.append(row[0])
    
    for record in records:
        txtReceipt.insert(END, "ID:"+str(record[-1])+ "\n" +"Name: "+str(record[0])+ "      " + "Phone: "+str(record[1]) + "\n")
        txtReceipt.insert(END, "----------------------------------------------" + "\n")
        
        for i, pasta_name in enumerate(pasta_names, start=2):  # Adjust the start index based on your actual data structure
            qty_index = i
            price_index = i + 13  # Adjust this as necessary
            if record[qty_index] > 0:
                txtReceipt.insert(END, f"{pasta_name}\t\t\t\t{record[qty_index]}x {record[price_index]}\n")
                
        txtReceipt.insert(END, "Total Cost:" + "\t\t\t\t" + str(record[14]) + "\n\n\n")  # Adjust index for total cost if needed
    
    conn.close()
