import tkinter as tk
from tkinter import ttk, messagebox

BG_COLOUR = "orange"
FG_COLOUR = "white"
BORDER_COLOUR = "black"

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
    text="End Program", 
    bg=BG_COLOUR,                # Background Color
    fg=FG_COLOUR,                 # Text Color
    bd=0,                       # Remove default button border
)

finish_btn.grid(row=9, column=1, pady=10)
finish_frame.grid(row=9, column=1, pady=10)

root.mainloop()
