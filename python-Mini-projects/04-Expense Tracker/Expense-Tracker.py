Expense = {
    1:{
        "amount":500,
        "category":"Food",
        "description":"Lunch",
        "date": "03-10-2026"
    },

    2:{
        "amount":600, 
        "category":"Food",
        "description":"breakfast",
        "date":"03-10-2026"
    }   
}


def Add_Expense():
    amount = int(input("Enter Amount   : "))
    category = input("Enter Category   : ")
    descrip = input("Enter Description : ")
    date = input("Enter Date           : ")

    Expense[len(Expense) + 1] = {
        "amount": amount,
        "category": category,
        "description": descrip,
        "date": date
    }

    print("added completed")
    return


def View_Expenses():
    if len(Expense) == 0:
        print("NO expense is add still")
        return

    print("======= Here All Expenses =======")

    for i , expense in Expense.items():
        print(f"Expense ID : {i}")
        print(f"Amount     :{expense['amount']}")
        print(f"Category   : {expense['category']}")
        print(f"Desciption : {expense['description']}")
        print(f"Date       : {expense['date']}")
        print()



def Total_amount():

    if len(Expense) == 0:
        print("No Expense isstlll add")
        return

    total = 0
    for i , expense in Expense.items():
        total += expense["amount"]

    print(f"Total amount is : {total}")
    print()

    return total

def Total_by_Category():

    if len(Expense) == 0:
        print("NO expense still add ")
        return

    category = input("Enter a Category : ")
    print()
    total = 0

    istrue = False

    for id, expense in Expense.items():
        if expense["category"] == category:
            total += expense['amount']
            istrue = True

    if istrue:
        print(f"For the Category : {category}")
        print(f"Total Amount is  : {total}")
    else:
        print(f"NO Category like : {category}")

def Highest_Expense():
    if len(Expense) == 0:
       print("NO Expense still added ")
       return

    high_amount = Expense[1]['amount']
    high_amount_ID = 1
    for ID , expense in Expense.items():

        if high_amount < expense['amount']:
            high_amount = expense['amount']
            high_amount_ID = ID

    print("Highest Expense")
    print(f"ID          : {high_amount_ID}")
    print(f"Amount      : {Expense[high_amount_ID]['amount']}")
    print(f"Category    : {Expense[high_amount_ID]['category']}")
    print(f"Description : {Expense[high_amount_ID]['description']}")
    print(f"Date        : {Expense[high_amount_ID]['date']}")
    print()


def Lowest_Expense():
    if len(Expense) == 0:
        print("NO Expense is added")
        return

    low_amount = Expense[1]['amount']
    low_amount_id = 1

    for ID , expense in Expense.items():

        if low_amount > expense['amount']:
            low_amount = expense['amount']
            low_amount_id = ID

    print("Lowest Expense")
    print(f"ID          : {low_amount_id}")
    print(f"Amount      : {Expense[low_amount_id]['amount']}")
    print(f"Category    : {Expense[low_amount_id]['category']}")
    print(f"Description : {Expense[low_amount_id]['description']}")
    print(f"Date        : {Expense[low_amount_id]['date']}")
    print()


def Average_Expense():

    if len(Expense) == 0:
        print("NO Expence is added")
        return
    total_expense = len(Expense)
    sum_amount = Total_amount()

    print("====== Average Expense ======")
    print(f"Total Expenses : {total_expense}")
    print(f"Total Amount   : ${sum_amount}")
    print(f"Average Expense : {sum_amount/total_expense}")


print("welcome to expense tracker")
while(True):
    print("1. add expense")
    print("2. view all expenses")
    print("3. Get total Amount")
    print("4. Total by Category")
    print("5. Check Highest Expense")
    print("6. Average Expense")
    choise = int(input("Enter ur choise : "))
    print()

    match choise:
        case 1:
            Add_Expense()
        case 2: 
            View_Expenses()
        case 3:
            Total_amount()
        case 4: 
            Total_by_Category()
        case 5:
            Highest_Expense()
        case 6:
            Average_Expense()
