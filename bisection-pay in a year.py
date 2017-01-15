# -*- coding: utf-8 -*-
balance = 320000
annualInterestRate = 0.2
r=annualInterestRate #annualInterestRate=18%
c=r/12 #monthlyPaymentRate=annualInterestRate/12

low=0.0 #浮点数运算关键
high=balance
while True:   
    b=balance
    pr=(high+low)/2
    for month in range(12):
        ub=b-pr
        b=(1+c)*ub
    if abs(b)<=0.01:
        break
    elif b>0.01:
        low=pr
    else:
        high=pr
    if high-low<0.01:
        break
print "Lowest Payment: "+str(pr)
    