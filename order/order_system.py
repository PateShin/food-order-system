from tkinter import *
from tkinter import messagebox
from order.submitorder.order_submission import submit_pick_order, submit_delivery_order
import csv


class OrderSystem:
    def read_pasta_names(self, filename):
        pasta_names = []
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header
            for row in reader:
                pasta_names.append(row[0])
        return pasta_names

    def __init__(self, root):
        self.root = root
        self.root.geometry("1338x700")
        self.root.title("Ordering System")
        self.root.configure(background='black')
        self.root.resizable(False, False)
        self.E_PASTA1 = IntVar(value=0)
        self.E_PASTA2 = IntVar(value=0)
        self.E_PASTA3 = IntVar(value=0)
        self.E_PASTA4 = IntVar(value=0)
        self.E_PASTA5 = IntVar(value=0)
        self.E_PASTA6 = IntVar(value=0)
        self.E_PASTA7 = IntVar(value=0)
        self.E_PASTA8 = IntVar(value=0)
        self.E_PASTA9 = IntVar(value=0)
        self.E_PASTA10 = IntVar(value=0)
        self.E_PASTA11 = IntVar(value=0)
        self.E_PASTA12 = IntVar(value=0)

        self.tem1 = StringVar()
        self.tem2 = StringVar()
        self.tem3 = StringVar()
        self.tem4 = StringVar()
        self.tem5 = StringVar()
        self.tem6 = StringVar()
        self.tem7 = StringVar()
        self.tem8 = StringVar()
        self.tem9 = StringVar()
        self.tem10 = StringVar()
        self.tem11 = StringVar()
        self.tem12 = StringVar()

        self.pasta_names = self.read_pasta_names('data/pasta_name.csv')
        # ----------------------Frame-------------------------------

        f1 = Frame(root, width=900, height=650, bd=8, relief="raised")
        f1.pack(side=LEFT)

        f1a = Frame(f1, width=900, height=330, bd=8, relief="raised")
        f1a.pack(side=TOP)

        f1aa = Frame(f1a, width=450, height=330, bd=16, relief="raised")
        f1aa.pack(side=LEFT)

        f1ab = Frame(f1a, width=450, height=330, bd=16, relief="raised")
        f1ab.pack(side=RIGHT)

        f2a = Frame(f1, width=900, height=320, bd=6, relief="raised")
        f2a.pack(side=BOTTOM)

        f2aa = Frame(f2a, width=450, height=330, bd=14, relief="raised")
        f2aa.pack(side=LEFT)

        f2ab = Frame(f2a, width=450, height=330, bd=14, relief="raised")
        f2ab.pack(side=RIGHT)

        f2abb = Frame(f2ab, width=300, height=250, bd=14, relief="raised")
        f2abb.pack(side=TOP)

        f2aab = Frame(f2ab, width=350, height=250, bd=14)
        f2aab.pack(side=BOTTOM)

        f2 = Frame(root, width=440, height=650, bd=8, relief="raised")
        f2.pack(side=RIGHT)

        ft2 = Frame(f2, width=440, height=450, bd=12, relief="raised")
        ft2.pack(side=TOP)

        fb2 = Frame(f2, width=440, height=300, bd=16, relief="raised")
        fb2.pack(side=BOTTOM)

        pasta_details = []
        for i, pasta_name in enumerate(self.pasta_names):
            frame = f1aa if i < 6 else f1ab  # Conditionally assign frame based on index
            pasta_details.append(
                (f"{pasta_name} \t", frame, getattr(self, f'E_PASTA{i + 1}'), getattr(self, f'tem{i + 1}')))

        def submit():
            order_type = typop.get()
            if order_type not in ["PICK", "DEL"]:
                messagebox.showinfo("Warning", "Please Select one of Pick up or Delivery Button")
                return

            res = messagebox.askquestion("Confirmation", "Are you sure?")
            if res != 'yes':
                messagebox.showinfo("Cancelled", "Ordering has been cancelled")
                return

            # Prepare the data for database submission
            data = {
                'entnme': Name.get(),
                'entphn': Phone.get(),
                'entadr': Address.get() if order_type == "DEL" else "",  # Address only needed for delivery
                'entfnum1': self.E_PASTA1.get(),
                'entfnum2': self.E_PASTA2.get(),
                'entfnum3': self.E_PASTA3.get(),
                'entfnum4': self.E_PASTA4.get(),
                'entfnum5': self.E_PASTA5.get(),
                'entfnum6': self.E_PASTA6.get(),
                'entfnum7': self.E_PASTA7.get(),
                'entfnum8': self.E_PASTA8.get(),
                'entfnum9': self.E_PASTA9.get(),
                'entfnum10': self.E_PASTA10.get(),
                'entfnum11': self.E_PASTA11.get(),
                'entfnum12': self.E_PASTA12.get(),
                'TotalCost': TotalCost.get(),
                'exdel': exdel.get() if order_type == "DEL" else "0",  # Extra delivery cost, if applicable
                'tem1': self.tem1.get(),
                'tem2': self.tem2.get(),
                'tem3': self.tem3.get(),
                'tem4': self.tem4.get(),
                'tem5': self.tem5.get(),
                'tem6': self.tem6.get(),
                'tem7': self.tem7.get(),
                'tem8': self.tem8.get(),
                'tem9': self.tem9.get(),
                'tem10': self.tem10.get(),
                'tem11': self.tem11.get(),
                'tem12': self.tem12.get(),
            }

            if order_type == "PICK":
                submit_pick_order(data)
            elif order_type == "DEL":
                submit_delivery_order(data)

            q_reset()

        def i_exit():
            iExit = messagebox.askyesno("Quit System", "Are you sure to Exit?")
            if iExit > 0:
                self.root.destroy()
                import main

        def q_reset():
            # Reset simple string variables
            for variable in [paid_tax, TotalCost, Name, Phone, Address]:
                variable.set("")

            # Reset pasta quantities and disable corresponding entry widgets
            pasta_vars = [self.E_PASTA1, self.E_PASTA2, self.E_PASTA3, self.E_PASTA4, self.E_PASTA5, self.E_PASTA6,
                          self.E_PASTA7, self.E_PASTA8, self.E_PASTA9, self.E_PASTA10, self.E_PASTA11, self.E_PASTA12]

            for var in pasta_vars:
                var.set("0")

            # Clear the receipt text
            txtReceipt.delete("1.0", END)

        def calculate_item_cost(quantity, price):
            """Calculate the cost of an item."""
            return quantity * price

        def format_currency(amount):
            """Format a number into currency format."""
            return "${:.2f}".format(amount)

        def update_ui(tem_variables, costs):
            """Update the UI with the calculated costs."""
            for tem_variable, cost in zip(tem_variables, costs):
                tem_variable.set(format_currency(cost))

        def calculate_total_cost(item_costs, extra_cost=0, tax_rate=0.15):
            """Calculate the total cost including tax and extra costs."""
            subtotal = sum(item_costs)
            tax = subtotal * tax_rate
            total_cost = subtotal + tax + extra_cost
            return tax, total_cost

        def CostOfItem():
            item_prices = [5, 5, 5, 5, 5, 5, 8, 8, 8, 8, 9, 9]
            tem_variables = [self.tem1, self.tem2, self.tem3, self.tem4, self.tem5, self.tem6, self.tem7, self.tem8,
                             self.tem9, self.tem10, self.tem11, self.tem12]
            e_pasta_variables = [self.E_PASTA1, self.E_PASTA2, self.E_PASTA3, self.E_PASTA4, self.E_PASTA5,
                                 self.E_PASTA6, self.E_PASTA7, self.E_PASTA8, self.E_PASTA9, self.E_PASTA10,
                                 self.E_PASTA11, self.E_PASTA12]
            item_costs = [calculate_item_cost(float(e_pasta.get()), price) for e_pasta, price in
                          zip(e_pasta_variables, item_prices)]
            update_ui(tem_variables, item_costs)

            delivery_type = typop.get()
            if delivery_type not in ["DEL", "PICK"]:
                messagebox.showinfo("Warning", "Please Select one of Pick up or Delivery Button")
                return

            extra_cost = 3 if delivery_type == "DEL" else 0
            if extra_cost:
                exdel.set(format_currency(extra_cost))

            tax, total_cost = calculate_total_cost(item_costs, extra_cost)

            paid_tax.set(format_currency(tax))
            TotalCost.set(format_currency(total_cost))

        def receipt():
            # Start by clearing the receipt
            txtReceipt.delete("1.0", END)

            # Insert pasta details into the receipt
            for pasta, _, e_pasta, tem in pasta_details:
                txtReceipt.insert(END, f'{pasta} \t\t {e_pasta.get()}\t{tem.get()}\n')

            txtReceipt.insert(END, f'---------------------\n')

            # Conditionally add delivery cost if delivery is selected
            if typop.get() == "DEL":
                txtReceipt.insert(END, f'Delivery Cost \t\t\t\t {exdel.get()}\n')

            # Add tax and total cost details
            txtReceipt.insert(END, f'Tax Paid \t\t\t\t {paid_tax.get()}\n')
            txtReceipt.insert(END, f'Total Cost \t\t\t\t {TotalCost.get()}\n')

        def validate_phone_number(action, value_if_allowed, prior_value, text, validation_type, trigger_type,
                                  widget_name):
            if action == '1':  # action 1 is insert
                if text in '0123456789':
                    # Check if the result of insertion would be valid
                    new_value = value_if_allowed
                    return len(new_value) <= 16
                else:
                    # Reject the character if it's not a number
                    return False
            else:
                # Allow deletion
                return True

        exdel = StringVar()
        paid_tax = StringVar()
        TotalCost = StringVar()
        Name = StringVar()
        Phone = StringVar()
        Address = StringVar()

        # Loop through each pasta detail and create a Label and Spinbox for it
        for i, (pasta_name, frame, text_variable, _) in enumerate(pasta_details):
            # Create Label
            Label(frame, text=pasta_name, font=('arial', 18, 'bold')).grid(row=i, sticky=W)
            # Create Spinbox
            Spinbox(frame, font=("arial", 16, "bold"), bd=8, width=6, textvariable=text_variable,
                    justify='left', from_=0, to=5).grid(row=i, column=1)
        # -----------------------------------------------------------------------------------------------------------------------------------
        lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Restaurant Receipt ", bd=2)
        lblReceipt.grid(row=0, column=0, sticky=W)
        txtReceipt = Text(ft2, font=('arial', 11, 'bold'), bd=8, width=40)
        txtReceipt.grid(row=1, column=0)
        # ---------------------------------------------------------------------------------------------------------------------------------
        lblCostOfFoods = Label(f2aa, font=('arial', 16, 'bold'), text="Total: ", bd=8)
        lblCostOfFoods.grid(row=0, column=0, sticky=W)

        txtCostOfFoods = Entry(f2aa, font=('arial', 16, 'bold'), bd=6, width=22, justify="left", textvariable=TotalCost,
                               state="disabled")
        txtCostOfFoods.grid(row=0, column=1, sticky=W)

        nme = Label(f2aa, font=('arial', 16, 'bold'), text="Name ", bd=8)
        nme.grid(row=1, column=0, sticky=W)

        entnme = Entry(f2aa, font=('arial', 16, 'bold'), bd=7, width=22, justify='left', textvariable=Name)
        entnme.grid(row=1, column=1, sticky=W)

        phn = Label(f2aa, font=('arial', 16, 'bold'), text="Phone number", bd=8)
        phn.grid(row=2, column=0, sticky=W)

        vcmd = f2aa.register(validate_phone_number)

        entphn = Entry(f2aa, font=('arial', 16, 'bold'), bd=6, width=22, justify='left', textvariable=Phone,
                       validate="key", validatecommand=(vcmd, '%d', '%P', '%s', '%S', '%v', '%V', '%W'))
        entphn.grid(row=2, column=1, sticky=W)

        adr = Label(f2aa, font=('arial', 16, 'bold'), text="Address", bd=8)
        adr.grid(row=3, column=0, sticky=W)

        entadr = Entry(f2aa, font=("arial", 16, "bold"), bd=6, width=22, justify='left', textvariable=Address)
        entadr.grid(row=3, column=1, sticky=W)
        typop = StringVar()

        pick = Radiobutton(f2abb, font=('arial', 14), text="Pick up", value="PICK", variable=typop, fg="green",
                           cursor="dot", padx=20)
        dev = Radiobutton(f2abb, font=('arial', 14), text="Delivery", value="DEL", variable=typop, fg="red",
                          cursor="dot", padx=20)
        pick.grid(row=2, column=0, sticky=W)
        dev.grid(row=2, column=1, sticky=W)

        Button(f2aab, padx=10, pady=10, bd=10, fg="black", font=('arial', 16, 'bold'), width=12,
               text="Total", command=CostOfItem).grid(row=0, column=0)
        Button(f2aab, padx=10, pady=10, bd=10, fg="black", font=('arial', 16, 'bold'), width=12,
               text="Receipt", command=receipt).grid(row=0, column=1)

        Button(fb2, font=('arial', 16, 'bold'), bd=6, width=24, justify='left', text="Submit", command=submit).grid(
            row=0, column=0, sticky=W)
        Button(fb2, bd=6, font=('arial', 16, 'bold'), width=24, justify="left", text="Reset",
               command=q_reset).grid(row=1, column=0)
        Button(fb2, bd=6, font=('arial', 16, 'bold'), width=24, justify="left", text="Exit",
               command=i_exit).grid(row=2, column=0)


if __name__ == '__main__':
    root = Tk()
    application = OrderSystem(root)
    root.mainloop()
