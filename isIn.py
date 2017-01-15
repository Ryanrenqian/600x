def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    if aStr =='':
        return False
    lenth=len(aStr)
    if lenth==1:
        return aStr==char
    if aStr[lenth/2]==char:
        return True
    elif char<aStr[lenth/2]:
        return isIn(char,aStr[:lenth/2])
    elif aStr[lenth/2]<char:
        return isIn(char,aStr[lenth/2:])

    else:
        return False