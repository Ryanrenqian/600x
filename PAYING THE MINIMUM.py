balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
r=annualInterestRate #annualInterestRate=18%
c=r/12 #monthlyPaymentRate=annualInterestRate/12
pr=monthlyPaymentRate #monthlypayrate=2%
b=balance #updatebalance=balance-monthlypayrate*balance
up=0
for month in range(12):
    ub=round(b-pr*b,2)
    up+=round(pr*b,2)
    print"Month: "+str(month+1)
    print"Minimum monthly payment:"+str(pr*b)    
    b=round(ub+c*ub,2)
    print"Remaining balance: "+str(b)
print "Total paid: "+str(up)
print "Remaining balance: "+str(b)
    