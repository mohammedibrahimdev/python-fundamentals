class ATM:

    def __init__ (self):

        self.__pin = ""
        self.__balance = 0

            
        self.menu()

    def menu(self):
        print("welcome to ATM")
        print("1. Enter to create PIN")
        print("2. Enter to deposit")
        print("3. Enter to withdrawal")
        print("4. Enter to check balance")
        print("5. Exit")
        choise = int(input("Enter ur choise : "))

        match choise:
            case 1:
                self.create_PIN()
            case 2:
                self.deposit()
            case 3:
                self.withdrawal()
            case 4:
                self.display_balance()
            case 5:
                exit

    def create_PIN(self):
        self.__pin = input("Enter ur PIN : ")
        print("PIN SEt")

    def deposit(self):
        temp = input("Enter ur PIN")

        if temp == self.__pin:
            amount = int(input("Enter amount to deposit : "))
            self.balance += amount
            print("deposited successfully")
        else:
            print("Invalid PIN")

    def withdrawal(self):
        temp = input("Enter ur PIN")

        if temp == self.__pin:
            amount = int(input("Enter amout to withdrawal : "))
            if amount <= self.__balance:
                self.balance -= amount
                print("withdrawal successfully")
            else:
                print("Insufficient money")
        else:
            print("Invalid PIN")

    def display_balance(self):

        temp = input("Enter PIN")
        if temp == self.__pin:
            print(f"balance : {self.__balance}")
obj = ATM()

obj.pi