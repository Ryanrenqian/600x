def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    '''
    c=min(a,b)
    d=max(a,b)
    if d%c==0:
        return c
    else:
        return gcdRecur(d,d%c)
    '''
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)