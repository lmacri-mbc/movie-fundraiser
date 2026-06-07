import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

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
BG_COLOUR = "orange"
FG_COLOUR = "white"
BORDER_COLOUR = "black"

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

def save_to_file(output):
    file = open('movie_data.txt', 'w')
    file.write(output)
    file.close()


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

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

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

        if all_ticket_costs[i] == 10.5:
            profit = 5.5
        elif all_ticket_costs[i] == 7.5:
            profit = 2.5
        else:
            profit = 1.5

        total_profit += profit

        output += f"{all_names[i]:<11} {to_currency(all_ticket_costs[i]):<14} {to_currency(all_surcharges[i]):<12} {to_currency(total_paid):<10} {to_currency(profit)}\n"

    output += "Total Paid: " + to_currency(total_collected) + "\n"
    output += "Total Profit: " + to_currency(total_profit)
    save_to_file(output)

###### Define TKinter GUI ######
root = tk.Tk()
root.title("Mini-Movie Fundraiser")
root.geometry("320x275")
root.configure(bg=BG_COLOUR)

title_label = ttk.Label(root, text="Mini-Movie Fundraiser", borderwidth=1, relief="solid", font=("Verdana", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
title_label.config(background=BG_COLOUR)
title_label.config(foreground=FG_COLOUR)

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

###### Create Buttons######
def create_frame(bg_color, border_color, border_width):
    '''This function will create a frame to give a black border around a button.'''
    new_frame = tk.Frame(root, bg=bg_color, highlightbackground=border_color, highlightthickness=border_width, bd=0)
    return new_frame


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
    command=end_program,
    text="End Program", 
    bg=BG_COLOUR,                # Background Color
    fg=FG_COLOUR,                 # Text Color
    bd=0,                       # Remove default button border
)

finish_btn.grid(row=9, column=1, pady=10)
finish_frame.grid(row=9, column=1, pady=10)

root.mainloop()
