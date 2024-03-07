from tkinter import *
from order.order_system import OrderSystem
from receipt.order_summary_gui import CustomerDetails


class OrderingSystemHome:
    def __init__(self):
        self.root = Tk()
        self.root.title('Ordering System Home')
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.create_widgets()
        self.create_frames()
        self.create_label()
        self.create_buttons()

        self.root.mainloop()

    def create_widgets(self):
        pass  # No widgets directly created in the class

    def create_frames(self):
        self.fr = Frame(self.root, width=100, height=60, bd=8, relief="solid")
        self.fr.grid(column=0, row=0, columnspan=2)

        self.ft = Frame(self.root, width=80, height=80, bd=8, relief="raised")
        self.ft.grid(column=0, row=1, columnspan=2, padx=115, pady=30)

    def create_label(self):
        self.t1t = Label(self.fr, font=('arial', 40, 'bold'), text=" Home ", bd=10)
        self.t1t.grid(column=0, row=0)

    def create_buttons(self):
        self.btn = Button(self.ft, text="New Order", command=self.open_new_order)
        self.btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        self.btn1 = Button(self.ft, text="View Customer Details", command=self.open_customer_details)
        self.btn1.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

    def open_new_order(self):
        self.root.destroy()
        new_root = Tk()
        application = OrderSystem(new_root)
        application.root.mainloop()

    def open_customer_details(self):
        self.root.destroy()
        new_root = Tk()
        customer_details = CustomerDetails(new_root)
        customer_details.window.mainloop()


# Run the application

ordering_system_home = OrderingSystemHome()
