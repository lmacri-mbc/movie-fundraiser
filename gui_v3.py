import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Housekeeping
# Program constants
# -----------------------------
MAX_TICKETS = 5
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50
CREDIT_SURCHARGE = 0.05
PAYMENT_TYPES = ('cash', 'credit')

# Data lists
all_names = []
all_ticket_costs = []
all_surcharges = []

tickets_sold = 0


def check_age(age):
    '''
        This checks that the user has entered valid data.
        Age cannot be less than 12, or older than 114.
    '''
    try:
        new_age = int(age)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter an integer (i.e. a number which doesn't have a decimal).")
        return -1

    if new_age < 12:
        messagebox.showerror("Error", "This customer is too young.")
        return -1
    elif new_age < 16:
        return CHILD_PRICE
    elif new_age < 65:
        return ADULT_PRICE
    else:
        return SENIOR_PRICE


def submit_ticket():
    name = name_entry.get().strip()
    pay_method = pay_method_box.get()
    age = age_entry.get().strip()

    if name == "":
        messagebox.showerror("Input Error", "Name cannot be blank.")
        return
    
    ticket_price = check_age(age)

    if ticket_price == -1:
        return

    all_names.append(name)
    all_ticket_costs.append(ticket_price)

    if pay_method == PAYMENT_TYPES[0]:
        all_surcharges.append(0)
    else:
        all_surcharges.append(CREDIT_SURCHARGE)


    

        

root = tk.Tk()
root.title("Mini-Movie Fundraiser")
root.geometry("300x300")

title_label = ttk.Label(root, text="Mini-Movie Fundraiser", font=("Verdana", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
name_entry = ttk.Entry(root, width=25)
name_entry.grid(row=1, column=1)

ttk.Label(root, text="Age:").grid(row=2, column=0, sticky="e")
age_entry = ttk.Entry(root, width=15)
age_entry.grid(row=2, column=1)

ttk.Label(root, text="Payment Method:").grid(row=3, column=0, sticky="e")
pay_method_box = ttk.Combobox(root, values=["cash", "credit"], state="readonly")
pay_method_box.grid(row=3, column=1)
pay_method_box.current(0)

submit_btn = ttk.Button(root, text="Submit Ticket", command=submit_ticket)
submit_btn.grid(row=4, column=0, pady=10)

finish_btn = ttk.Button(root, text="Finish Early")
finish_btn.grid(row=4, column=1, pady=10)

root.mainloop()
