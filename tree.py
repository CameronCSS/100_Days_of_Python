'''
Given an input n print out a tree of height n

Example:
n = 5


    *
   ***        
  *****       
 *******      
********* 
'''


def tree(n):
    for i in range(n):
        spaces = n - i - 1
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars)
    
    
    
tree(5)
tree(10)