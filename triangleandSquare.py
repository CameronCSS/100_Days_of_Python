# Draw A Triangle of n height
# *
# **
# ***
# ****
# *****

# Draw A Square of n height
# xxxxx
# x   x
# x   x
# x   x
# xxxxx

X = 6

def triangle(n) -> None:    
    for i in range(n):
        i += 1
        print("*" * i)
    return

def square(n) -> None:    
    for i in range(n):
        if i == 0 or i == n - 1:
            print("x" * n)
        else:
            row = "x" + " " * (n - 2) + "x"
            print(row)
    return



triangle(X)
square(X)