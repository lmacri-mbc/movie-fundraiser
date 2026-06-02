import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Housekeeping
# Program constants
# -----------------------------
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

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
    elif new_age < 115:
        return SENIOR_PRICE
    else:
        return -1