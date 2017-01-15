def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    for i in range(n/20,-1,-1):
        c=n-i*20
#        print "c="+str(c)
        if c==0:
            return True
        else:
            for k in range(c/9,-1,-1):
                b=c-k*9
#                print "b="+str(b)
                if b==0:
                    return True
                else:
                    for j in range(b/6,-1,-1):
                        a=b-j*6
#                        print "a=",a
                        if a==0:
                            return True
    return False
            
        
    