# Armstron number identifier
# functions, for loops, lists, if-else statements

 
def length(user_number):
    n = len(user_number)
    x.append(n)
    
def indiv_number(user_number):
    for m in user_number:
        m = int(m)
        y.append(m)

def anumber(x, y):
    for i in y:
        i = i**x[0]
        z.append(i)
x = []
y = []
z = []

user_name = input('Enter name: ')
print(f"Hi, {user_name.title()}!")
print("\nI can tell you whether a number is Armstrong number or not")
user_number = input('Enter number: ')

length(user_number)
indiv_number(user_number)
anumber(x, y)

final_number = str(sum(z))
if final_number == user_number:
    print(f"\nThe number {user_number} is an Armstrong number!")
else:
    print(f"\nThe number {user_number} is not an Armstrong number :(")

    
print("\n---Results---")
print(f"Exponent: {x}")
print(f"Digit/s: {y}")
print(f"Digits raised to the power of {x[0]}: {z}")
print(f"Sum of digits raised to the power of {x[0]}: {final_number}")

