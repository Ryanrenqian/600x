def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    lenth1=len(s1)
    lenth2=len(s2)
    string=''
    lenth=0
    s3=''
    if lenth1>lenth2:
        lenth=lenth2
        s3=s1[lenth2:lenth1]
    else:
        lenth=lenth1
        s3=s2[lenth1:lenth2]
    for i in range(lenth):
        string+=s1[i]+s2[i]
    string+=s3
    return string