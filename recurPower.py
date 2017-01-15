def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    '''
    if exp==0:
        return 1
    else:
        ans=base*recurPower(base,exp-1)
    return ans
    '''
    if exp==0:
        return 1
    elif exp>0 and exp%2==0:
        return recurPower(base**2,exp/2)
    elif exp>0  and exp%2==1:
        return base*recurPower(base,exp-1)
    