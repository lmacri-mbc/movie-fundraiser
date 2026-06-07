from datetime import date

CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

### Helper Functions ###
def to_currency(x):
    return "${:.2f}".format(x)

def make_statement(statement, decoration):
    return f"{decoration * 3} {statement} {decoration * 3}"

def save_to_file(output):
    file = open('movie_data.txt', 'w')
    file.write(output)
    file.close()


def print_to_file(all_names, all_ticket_costs, all_surcharges):
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

all_names = ["A", "B", "C", "D", "E"]
all_ticket_costs = [7.5, 7.5, 10.5, 10.5, 6.5]
all_surcharges = [0, 0.38, 0, 0.53, 0]

print_to_file(all_names, all_ticket_costs, all_surcharges)

