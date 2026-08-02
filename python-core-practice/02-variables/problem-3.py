"""""
Problem 3: Swap two numbers

Take two variable a and b
Take anothe variable call temp
temp = a
a = b
b = temp
 -print again a and b after Swap

Note:
f-string (Formatted String)
An f-string is a way to insert the values of variables directly inside a string using {}.
"""""

a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))

print(f"Before swap : a = {a} , b = {b}")
temp = a
a = b
b = temp
print(f"After swap : a = {a},b = {b}")

