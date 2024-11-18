def add_nums(*args):
    
    total = 0
    for num in args:
        total += num
        
    print(total)
        
        
        
add_nums(1,4,5,7)


def calculate(n, **kw):
    print(f"The number is {n}")
    n += kw.get('add')
    print(f"When you add {kw.get('add')} you get {n}")
    n *= kw.get('multiply')
    print(f"After you multiply by {kw.get('multiply')} you get {n}")
    
    
calculate(2, add=3, multiply=5)