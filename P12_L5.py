def genPrimes():
    prime=[2]
    n=1

    while True:
        lenth=len(prime)
        for i in prime:

            if n%i!=0:
                lenth-=1
        if lenth==0 or n==2:
            next=n
            yield next
            prime.append(next)
        
        n+=1
        
prim=genPrimes()
prim.next()