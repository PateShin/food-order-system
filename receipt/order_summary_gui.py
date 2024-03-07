import sqlite3
from tkinter import *
from tkinter import messagebox
from receipt.ReceiveType.pickup import pickup
from receipt.ReceiveType.delivery import delivery


class CustomerDetails:
    def __init__(self, window):
        self.window = window
        self.window.title('Customers Detail.com')
        self.window.geometry("708x720")
        self.window.resizable(False, False)

        self.create_widgets()
        self.create_frames()
        self.create_labels()
        self.create_buttons()
        self.create_text_boxes()
        self.create_entry_boxes()

        self.window.mainloop()

    def create_widgets(self):
        pass  # No widgets directly created in the class

    def create_frames(self):
        self.ftitle = Frame(self.window, width=100, height=5, bd=8, relief="raised")
        self.ftitle.grid(column=0, row=0, columnspan=2)

        self.f1 = Frame(self.window, width=900, height=650, bd=8, relief="raised")
        self.f1.grid(column=0, row=2)

        # ... (similarly create remaining frames)

        self.f1a = Frame(self.f1, width=850, height=250, bd=8, relief="raised")
        self.f1a.pack(side=BOTTOM)

        self.f2 = Frame(self.window, width=900, height=650, bd=8, relief="raised")
        self.f2.grid(column=1, row=2)

        self.f2a = Frame(self.f2, width=850, height=250, bd=8, relief="raised")
        self.f2a.pack(side=BOTTOM)

        self.f3 = Frame(self.window, width=450, height=800, bd=8, relief="raised")
        self.f3.grid(column=0, row=1)

        self.f4 = Frame(self.window, width=450, height=800, bd=8, relief="raised")
        self.f4.grid(column=1, row=1)

        self.f5 = Frame(self.window, width=900, height=200, bd=8)
        self.f5.grid(column=0, row=3, columnspan=2)
        # --------------------------------------------

    def create_labels(self):
        self.tit = Label(self.ftitle, font=('arial', 15, 'bold'), text=" Customer Details ", bd=10)
        self.tit.grid(column=0, row=0)

        # ... (similarly create remaining labels)

    def create_buttons(self):
        self.delt = Button(self.f1a, text="DELETE", font=('Arial', 8, 'bold'), command=self.deletep)
        self.delt.grid(row=1, column=0, pady=5, padx=2, ipadx=100, columnspan=3)

        # ... (similarly create remaining buttons)
        delt1 = Button(self.f2a, text="DELETE", font=('Arial', 8, 'bold'), command=self.deleted)
        delt1.grid(row=1, column=0, pady=5, padx=2, ipadx=100, columnspan=3)

        submit_btn = Button(self.f1, text="REFRESH P", font=('Arial', 10, 'bold'),
                            command=lambda: pickup(self.txtReceipt), relief="raised", height=2, width=35)
        submit_btn.pack(side=TOP)

        query_btn = Button(self.f2, text="REFRESH D", font=('Arial', 10, 'bold'),
                           command=lambda: delivery(self.txtReceipt1), relief="raised", height=2, width=35)
        query_btn.pack(side=TOP)

        Exi = Button(self.f5, text="Exit", font=('Arial', 11, 'bold'), height=2, width=60, bg="red", command=self.rExit)
        Exi.pack(side=BOTTOM)

    def create_text_boxes(self):
        self.txtReceipt = Text(self.f3, font=('arial', 11, 'bold'), bd=8, width=40)
        self.txtReceipt.grid(row=1, column=0)

        self.txtReceipt1 = Text(self.f4, font=('arial', 11, 'bold'), bd=8, width=40)
        self.txtReceipt1.grid(row=1, column=0)

    def create_entry_boxes(self):
        self.delete_box = Entry(self.f1a, width=20)
        self.delete_box.grid(row=0, column=1)

        self.delete_box1 = Entry(self.f2a, width=20)
        self.delete_box1.grid(row=0, column=1)

    def deletep(self):
        self.txtReceipt.delete("1.0", END)
        conn = sqlite3.connect('data/Detail.db')
        c = conn.cursor()
        c.execute("DELETE from pick WHERE oid = " + self.delete_box.get())
        conn.commit()
        conn.close()

    def deleted(self):
        self.txtReceipt1.delete("1.0", END)
        conn = sqlite3.connect('data/Detail.db')
        c = conn.cursor()
        c.execute("DELETE from delivery WHERE oid = " + self.delete_box1.get())
        conn.commit()
        conn.close()

    def rExit(self):
        iExit = messagebox.askyesno("Quit System", "Do you want to quit?")
        if iExit > 0:
            self.window.destroy()
            import main


# Run the application
if __name__ == '__main__':
    root = Tk()
    customer_details = CustomerDetails(root)
    root.mainloop()
