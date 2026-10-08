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
    try:
        amount = float(input("Enter Amount   : "))
    except ValueError:
        print("Please Enter a valid number : \n")
        print()
        return

    if amount <= 0:
        print("Amount must be greater then 0")
        return
    
    category = input("Enter Category   : ")
    if  category == "":
        print("Category cannot be Empty\n")
        return
    descrip = input("Enter Description : ")
    if descrip == "":
        print("Desciptio cannot be Empty\n")
        return
    
    date = input("Enter Date           : ")
    if date == "":
        print("Date cannot be Empty")
        return
    
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

    for i, expense in Expense.items():
        print(f"Expense ID : {i}")
        print(f"Amount     : {expense['amount']}")
        print(f"Category   : {expense['category']}")
        print(f"Desciption : {expense['description']}")
        print(f"Date       : {expense['date']}")
        print()


def Total_amount():

    if len(Expense) == 0:
        print("No Expense isstlll add")
        return

    total = 0

    for i, expense in Expense.items():
        total += expense["amount"]

    print(f"Total amount is : {total}")
    print()

    return total


def Total_by_Category():

    if len(Expense) == 0:
        print("NO expense still add ")
        return

    category = input("Enter a Category : ")
    if category == "":
        print("Category cannot be Empty\n")
        return
    

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

    for ID, expense in Expense.items():

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

    for ID, expense in Expense.items():

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
    print(f"Average Expense : {sum_amount / total_expense}")


def search_by_category():

    category = input("Enter Category : ")
    if category == "":
        print("Category cannot be Empty")
        return
    
    found = True

    for ID, expense in Expense.items():

        if expense["category"] == category:

            print("========================")
            print("Searched by category : ")
            print(f"Expense ID  : {ID}")
            print(f"Amount      : {expense['amount']}")
            print(f"Category    : {expense['category']}")
            print(f"Description : {expense['description']}")
            print(f"Date        : {expense['date']}")
            print()

            found = False

    if found:
        print("Expense is not found")


def search_by_date():

    date = input("Enter Date : ")
    if date == "":
        print("Date cannot be Empty")
        return
    found = True

    for ID, expense in Expense.items():

        if expense['date'] == date:

            print("======================")
            print("Searched by Date ")
            print(f"Expense ID : {ID}")
            print(f"Amount : {expense['amount']}")
            print(f"Category : {expense['category']}")
            print(f"Description : {expense['description']}")
            print(f"Date : {expense['date']}")
            print()

            found = False

    if found:
        print("Expense is not found")


def search_by_amount():

    try:
        amount = int(input("Enter Amount "))
    except ValueError:
        print("Please Enter Valid Amount : ")
        return
    found = True

    for ID, expense in Expense.items():

        if expense['amount'] == amount:

            print("=====================")
            print("searched by Amount ")
            print(f"Expense ID  : {ID}")
            print(f"Amount      : {expense['amount']}")
            print(f"Category    : {expense['category']}")
            print(f"Description : {expense['description']}")
            print(f"Date        : {expense['date']}")

            found = False

    if found:
        print("Expense is not found")


def Search_Expenses():

    if len(Expense) == 0:
        print("NO Expense is added")
        return

    print("Search Expenses")
    print("1. By Category")
    print("2. By Date")
    print("3. By Amount")

    try:
        choise = int(input("Enter Your Choise : "))
    except ValueError:
        print("please Enter valid choise")
        print()
        return
    
    match choise:

        case 1:
            search_by_category()

        case 2:
            search_by_date()

        case 3:
            search_by_amount()


# ==============================
# SUB-FUNCTIONS OF EDIT EXPENSE
# ==============================

def edit_amount(ID, expense):
    
    try:
        amount = int(input("Enter Amount to Edit : "))
    except ValueError:
        print("Please Enter valid Amount")
        return
    
    previous_amount = expense['amount']

    expense['amount'] = amount

    print("Edited the amount : ")
    print(f"Previous Amount : {previous_amount}")
    print(f"New Amount      : {amount}")

    print("Edited successfully")


def edit_category(ID, expense):

    category = input("Enter Category to Edit : ")

    previous_category = expense['category']

    expense['category'] = category

    print("Edited the category : ")
    print(f"Previous Category : {previous_category}")
    print(f"New Category      : {category}")

    print("Edited successfully")


def edit_description(ID, expense):

    description = input("Enter Description to Edit : ")

    previous_description = expense['description']

    expense['description'] = description

    print("Edited the description : ")
    print(f"Previous Description : {previous_description}")
    print(f"New Description      : {description}")

    print("Edited successfully")


def edit_date(ID, expense):

    date = input("Enter Date to Edit : ")

    previous_date = expense['date']

    expense['date'] = date

    print("Edited the date : ")
    print(f"Previous Date : {previous_date}")
    print(f"New Date      : {date}")

    print("Edited successfully")


def Edit_Expenses():

    if len(Expense) == 0:
        print("No Expense is added")
        return
    try:
        ID = int(input("Enter Expense ID : "))
    except ValueError:
        print("Please Enter valid ID ")
        return
    
    # Check whether ID exists
    if ID not in Expense:
        print("Expense ID is not found")
        return

    # Get the expense directly
    expense = Expense[ID]

    print("Current Expense :")
    print(f"Amount     : {expense['amount']}")
    print(f"Category   : {expense['category']}")
    print(f"Description : {expense['description']}")
    print(f"Date       : {expense['date']}")

    print()

    print("Enter to Edit ")
    print("1. Edit Amount")
    print("2. Edit Category")
    print("3. Edit Description")
    print("4. Edit Date")

    try:
        choise = int(input("Enter here : "))
    except ValueError:
        print("Please Enter valid choise")
        print()
        return
    
    match choise:

        case 1:
            edit_amount(ID, expense)

        case 2:
            edit_category(ID, expense)

        case 3:
            edit_description(ID, expense)

        case 4:
            edit_date(ID, expense)


def delete_Expense():
    if len(Expense) == 0:
        print("there is no Expense")
        return

    try:
        id = int(input("Enter Expense ID : "))
        print()
    except ValueError:
        print("Please Enter valid ID : ")
        return

    if id not in Expense:
        print(f"Not found the Expense of ID : {id}")
        return

    expense = Expense[id]

    print("Expense: ")
    print(f"Amount      : {expense['amount']}")
    print(f"Category    : {expense['category']}")
    print(f"Description : {expense['description']}")
    print(f"Date        : {expense['date']}")
    print()

    sure = input("Are you sure you want to delete? (y/n): ")

    if sure == 'y' or sure == 'Y':
        del Expense[id]
        print("Expense Deleted successfully.")
    else:
        print("Expense is not Deleted")



# ==============================
# MAIN MENU
# ==============================

print("welcome to expense tracker")

while True:

    print("1. add expense")
    print("2. view all expenses")
    print("3. Get total Amount")
    print("4. Total by Category")
    print("5. Check Highest Expense")
    print("6. Average Expense")
    print("7. Lowest Expense")
    print("8. Search Expenses")
    print("9. Edit Expenses")
    print("10. Delete Expenses")

    try:
        choise = int(input("Enter ur choise : "))
        print()
    except ValueError:
        print("Please Enter valid choise : ")
        continue

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

        case 7:
            Lowest_Expense()

        case 8:
            Search_Expenses()

        case 9:
            Edit_Expenses()
        case 10:
            delete_Expense()