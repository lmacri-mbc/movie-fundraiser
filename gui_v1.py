import tkinter as tk
from tkinter import ttk, messagebox

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

submit_btn = ttk.Button(root, text="Submit Ticket")
submit_btn.grid(row=4, column=0, pady=10)

finish_btn = ttk.Button(root, text="Finish Early")
finish_btn.grid(row=4, column=1, pady=10)

root.mainloop()
