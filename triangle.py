'''
Given an input n print out a triangle of height n

Example:
n = 5

*
**
***
****
*****
'''


def triangle(n):
    for i in range(1, n + 1):
        print('*' * i)
    
triangle(5)
triangle(10)