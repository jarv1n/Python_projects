# 99 bottles 
# functions, list, if-elif-else statements

def botlle_99():
    for i in reversed(range(0, 100)):
        if i == 1:
            print(f"{i} {x[1]}, {i} {x[3]}.")
            print(f"{x[4]}, {x[6]}.\n")
        elif i == 2:
            print(f"{i} {x[0]}, {i} {x[2]}.")
            print(f"{x[4]}, {i - 1} {x[1]}.\n")  
        elif i == 0:
            print(f"{x[7]}, {x[8]}.")
            print(f"{x[5]}, {i + 99} {x[0]}.\n")
        else:
            print(f"{i} {x[0]}, {i} {x[2]}.")
            print(f"{x[4]}, {i -1} {x[0]}.\n")
            
x = [
    'bottles of beer on the wall',
    'bottle of beer on the wall',
    'bottles of beer',
    'bottle of beer',
    'Take one down and pass it around', 
    'Go to the store and buy some more',
    'no more bottles of beer on the wall',
    'No more bottles of beer on the wall',
    'no more bottles of beer'
]

botlle_99()
