"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract,comission,pay,comissionPay,hoursworked,noOfContracts):
        self.name = name
        self.contract = contract
        self.comission = comission
        self.pay=pay
        self.comissionPay=comissionPay
        self.hoursworked=hoursworked
        self.noOfContracts=noOfContracts

    def get_pay(self):
        totalPay =0
        if self.contract=='monthly':
            totalPay=totalPay+self.pay
        else:
            totalPay=totalPay+self.pay*self.hoursworked
        if self.comission=='contract':
            totalPay=totalPay+self.comissionPay*self.noOfContracts
        elif self.comission=='bonus':
            totalPay=totalPay+self.comissionPay
        
        return totalPay

    def __str__(self):
        statment=self.name
        if self.contract=='monthly':
            statment=statment+" works on a monthly salary of "+str(self.pay)
        else:
            statment=statment+" works on a contract of "+str(self.hoursworked)+" hours at "+str(self.pay)+"/hour"
        if self.comission=="contract":
            statment=statment+" and receives a commission for "+str(self.noOfContracts)+" contract(s) at "+str(self.comissionPay)+"/contract."
        elif self.comission=="bonus":
            statment=statment+" and receives a bonus commission of "+str(self.comissionPay)+"."
        else:
            statment=statment+"."
        statment=statment+"  Their total pay is "+str(self.get_pay())+"."

        return statment
    
    


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie','monthly','without',4000,None,None,None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie','hourly','without',25, None,100,None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee','monthly','contract',3000,200,None,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan','hourly','contract',25,220,150,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie','monthly','bonus',2000,1500,None,None)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel','hourly','bonus',30,600,120,None)

print(str(charlie))