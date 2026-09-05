people = []
expenses = []


def add_person():
    name = input("Enter person's name: ")

    if name in people:
        print("Person already exists!")
    else:
        people.append(name)
        print(name, "added successfully!")


def add_expense():
    if len(people) == 0:
        print("Please add people first!")
        return

    print("\nPeople:")
    for name in people:
        print("-", name)

    payer = input("Who paid? ")

    if payer not in people:
        print("Person not found!")
        return

    amount = float(input("Enter amount: "))
    description = input("Enter expense description: ")

    expenses.append([payer, amount, description])

    print("Expense added successfully!")


def view_expenses():
    print("\n========== ALL EXPENSES ==========")

    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    for expense in expenses:
        print(
            expense[0],
            "paid Rs.",
            expense[1],
            "for",
            expense[2]
        )


def calculate_split():
    if len(people) == 0:
        print("Please add people first!")
        return

    total = 0

    for expense in expenses:
        total = total + expense[1]

    share = total / len(people)

    print("\n========== SPLIT SUMMARY ==========")
    print("Total Expense: Rs.", total)
    print("Number of People:", len(people))
    print("Each Person Should Pay: Rs.", round(share, 2))

    print("\n========== BALANCE ==========")

    paid_amount = {}

    for person in people:
        paid_amount[person] = 0

    for expense in expenses:
        paid_amount[expense[0]] += expense[1]

    for person in people:
        balance = paid_amount[person] - share

        if balance > 0:
            print(person, "should receive Rs.", round(balance, 2))

        elif balance < 0:
            print(person, "should pay Rs.", round(-balance, 2))

        else:
            print(person, "is settled.")


while True:

    print("\n================================")
    print("        EXPENSE SPLITTER")
    print("================================")

    print("1. Add Person")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Calculate Split")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_person()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        view_expenses()

    elif choice == "4":
        calculate_split()

    elif choice == "5":
        print("Thank you for using Expense Splitter!")
        break

    else:
        print("Invalid choice!")