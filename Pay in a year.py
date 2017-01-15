balance = 4773
annualInterestRate = 0.2
#def Minpr(balance,annualInterestRate)
r=annualInterestRate #annualInterestRate=18%
c=r/12 #monthlyPaymentRate=annualInterestRate/12
#pr=10#balance/12 #monthlypayrate=2%
#b=balance #updatebalance=balance-monthlypayrate*balance
for pr in range(10,int(balance),10):
#while True:    
    b=balance
    for month in range(12):
        ub=b-pr
#        up+=round(pr*b,2)
#    print"Month: "+str(month+1)
#    print"Minimum monthly payment:"+str(pr*b)    
        b=(1+c)*ub
    if b<=0:
        #return "Lowest Payment:",pr
        break
#    else:
#        pr+=10
 #   print"Remaining balance: "+str(b)
#print "Total paid: "+str(up)
print "Remaining balance: "+str(pr)
#Minpr(balance,annualInterestRate)