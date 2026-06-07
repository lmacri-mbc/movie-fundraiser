CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

def to_currency(x):
    return "${:.2f}".format(x)

def print_to_file(all_names, all_ticket_costs, all_surcharges):
    total_tix_sold = len(all_names)
    total_profit = 0
    total_surcharge = 0
    total_paid = 0

    for i in range(total_tix_sold):
        profit = 0
        total_surcharge += all_surcharges[i]
        total_paid += all_ticket_costs[i] + all_surcharges[i]

        if all_ticket_costs[i] == 10.5:
            profit = 5.5
        elif all_ticket_costs[i] == 7.5:
            profit = 2.5
        else:
            profit = 1.5

        total_profit += profit

        print(f"{all_names[i]}  {to_currency(all_ticket_costs[i])}  {to_currency(all_surcharges[i])}  {to_currency(profit)}")

    print("Total Paid: " + to_currency(total_paid))
    print("Total Profit: " + to_currency(total_profit))

all_names = ["A", "B", "C", "D", "E"]
all_ticket_costs = [7.5, 7.5, 10.5, 10.5, 6.5]
all_surcharges = [0, 0.38, 0, 0.53, 0]

print_to_file(all_names, all_ticket_costs, all_surcharges)