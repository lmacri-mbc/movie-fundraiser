import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import random

# -----------------------------
# Housekeeping
# Program constants
# -----------------------------
MAX_TICKETS = 150
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50
CREDIT_SURCHARGE = 0.05
PAYMENT_TYPES = ('cash', 'credit')
BG_COLOUR = "orange"
FG_COLOUR = "white"
BORDER_COLOUR = "black"
MY_FONT=("Verdana", 18, "bold")

# Data lists
all_names = []
all_ticket_costs = []
all_surcharges = []

tickets_sold = 0

### Helper Functions ###
def to_currency(x):
    return "${:.2f}".format(x)

def make_statement(statement, decoration):
    return f"{decoration * 3} {statement} {decoration * 3}"

def create_frame(bg_color, border_color, border_width):
    '''This function will create a frame to give a black border around a button.'''
    new_frame = tk.Frame(root, bg=bg_color, highlightbackground=border_color, highlightthickness=border_width, bd=0)
    return new_frame

def save_to_file(output):
    file = open('movie_data.txt', 'w')
    file.write(output)
    file.close()

def show_instructions():
    instructions = '''
    For each ticket holder enter…
    -	Their name
    -	Their age
    -	The payment method (cash/credit)

    The program will record the ticket sale and calculate the ticket cost (and the profit).

    Once you have either sold all the tickets or entered the exit code (‘xxx’), the program will display the ticket sales info and write the data to a text file.

    It will also choose one lucky ticket holder who wins the draw (their ticket is free).
    '''
    messagebox.showinfo("Information", instructions)


def get_profit(ticket_price):
    if ticket_price == 10.5:
        return 5.5
    elif ticket_price == 7.5:
        return 2.5
    else:
        return 1.5


def check_age(age):
    '''
        This checks that the user has entered valid data.
        Age cannot be less than 12, or older than 114.
        It returns the ticket price or -1 for error
    '''
    try: # Test age is an integer.
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
    '''This function runs each time a ticket has been purchased. It gathers info
       from the GUI, calculated ticket price and surcharge and stores it in
       the above declared data lists.'''
    name = name_entry.get().strip()
    pay_method = pay_method_box.get()
    age = age_entry.get().strip()
    global tickets_sold

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
        all_surcharges.append(ticket_price * CREDIT_SURCHARGE)

    # Give system feedback
    tickets_sold += 1
    status_label.config(text=f"Tickets sold: {tickets_sold} / {MAX_TICKETS}")

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)


def test_final():
    names = ("A", "B", "C", "D", "E")
    ages = ("12", "15", "16", "64", "65")
    pay_method = ("cash", "credit", "cash", "credit", "cash")

    for i in range(5):
        name_entry.insert(0, names[i])
        age_entry.insert(0, ages[i])
        pay_method_box.set(pay_method[i])

        submit_ticket()

    end_program()

def end_program():
    total_tix_sold = len(all_names)
    total_profit = 0
    total_surcharge = 0
    total_paid = 0
    total_collected = 0

    today = date.today()
    heading = make_statement(f"Mini Movie Fundraiser Ticket Data ({today})", "=")
    output = heading + "\n"

    output += make_statement("Ticket Details", "-") + "\n\n"
    output += "Name  |  Ticket Price  |  Surcharge  |  Total  |  Profit \n"
    output += "-" * 55 + "\n"

    for i in range(total_tix_sold):
        profit = 0
        total_surcharge += all_surcharges[i]
        total_paid = all_ticket_costs[i] + all_surcharges[i]
        total_collected += total_paid

        profit = get_profit(all_ticket_costs[i])
        total_profit += profit

        output += f"{all_names[i]:<11} {to_currency(all_ticket_costs[i]):<14} {to_currency(all_surcharges[i]):<12} {to_currency(total_paid):<10} {to_currency(profit)}\n"

    output += "Total Paid: " + to_currency(total_collected) + "\n"
    output += "Total Profit: " + to_currency(total_profit)

    ### Choose lucky winner ###
    winner = random.choice(all_names)
    winner_index = all_names.index(winner)

    ticket_won = all_ticket_costs[winner_index]
    profit_won = get_profit(ticket_won)

    output += make_statement("Raffle Winner", "-")
    output += f"\nThe lucky winner is {winner}. Their ticket worth ${ticket_won:.2f} is free!\n\n"

    output += f"Adjusted Total Paid: ${total_collected - ticket_won:.2f}\n"
    output += f"Adjusted Profit: ${total_profit - profit_won:.2f}\n\n"

    if tickets_sold == MAX_TICKETS:
        output += make_statement(f"You have sold all {MAX_TICKETS} tickets", "-")
    else:
        output += make_statement(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets", "-")

    save_to_file(output)
    root.destroy()

###### Define TKinter GUI ######
root = tk.Tk()
root.title("Mini-Movie Fundraiser")
root.geometry("350x320")
root.configure(bg=BG_COLOUR)

###### Add app name label ######
title_label = ttk.Label(root, text="Mini-Movie Fundraiser", borderwidth=1, relief="solid", font=MY_FONT)
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
title_label.config(background=BG_COLOUR)
title_label.config(foreground=FG_COLOUR)

###### Add Help button ######
help_frame = create_frame(BG_COLOUR, BORDER_COLOUR, 2)
help_btn = tk.Button(
    help_frame, 
    command=show_instructions,
    text="?", 
    bg=BG_COLOUR,                # Background Color
    fg=FG_COLOUR,                 # Text Color
    bd=0,                       # Remove default button border
)

help_btn.grid(row=0, column=2)
help_frame.grid(row=0, column=2, pady=10)

###### Add name label and entry box ######
lbl_name = ttk.Label(root, text="Name:", borderwidth=2, relief="solid")
lbl_name.grid(row=1, column=0, sticky="w", padx=20, pady=20)
lbl_name.config(background=BG_COLOUR)

name_entry = ttk.Entry(root, width=25)
name_entry.grid(row=1, column=1, pady=20)

###### Add age label and entry box ######
lbl_age = ttk.Label(root, text="Age:", borderwidth=1, relief="solid")
lbl_age.grid(row=2, column=0, sticky="w", padx=20)
lbl_age.config(background=BG_COLOUR)

age_entry = ttk.Entry(root, width=25)
age_entry.grid(row=2, column=1)

#### Add payment lable and drop down ######
lbl_payment = ttk.Label(root, text="Payment Method:", borderwidth=1, relief="solid")
lbl_payment.grid(row=3, column=0, sticky="w", padx=20, pady=20)
lbl_payment.config(background=BG_COLOUR)

pay_method_box = ttk.Combobox(root, values=["cash", "credit"], state="readonly", width=22)
pay_method_box.grid(row=3, column=1, pady=20)
pay_method_box.current(0)


###### Add Submit button ######
submit_frame = create_frame(BG_COLOUR, BORDER_COLOUR, 2)
submit_btn = tk.Button(
    submit_frame, 
    command=submit_ticket,
    text="Submit Ticket", 
    bg=BG_COLOUR,                # Background Color
    fg=FG_COLOUR,                 # Text Color
    bd=0,                       # Remove default button border
)

submit_btn.grid(row=9, column=0, pady=10)
submit_frame.grid(row=9, column=0, pady=10)

###### Add Finish button ######
finish_frame = create_frame(BG_COLOUR, BORDER_COLOUR, 2)
finish_btn = tk.Button(
    finish_frame,
    command=test_final, # end_program,
    text="End Program", 
    bg=BG_COLOUR,                # Background Color
    fg=FG_COLOUR,                 # Text Color
    bd=0,                       # Remove default button border
)

finish_btn.grid(row=9, column=1, pady=10)
finish_frame.grid(row=9, column=1, pady=10)

status_label = ttk.Label(root, text=f"Tickets sold: 0 / {MAX_TICKETS}", font=MY_FONT)
status_label.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()
