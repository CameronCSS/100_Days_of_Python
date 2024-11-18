# Print a rectangle

# M is the width, N is the height
# M > 0, N > 0

# Example:
# m = 6
# N = 4

'''
******
*    *
*    *
******
'''


def rectangle(m,n):
    print('*' * m)
    for i in range(n-1):
        print('*', ' ' * (m - 4), '*') # The correct answer is really ' ' * (m-2) but for some reason in vs code the spacing doesnt look correct unless you do (m-4)
    print('*' * m)
            

rectangle(4,6)
print()
rectangle(7,10)