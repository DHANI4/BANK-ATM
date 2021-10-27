class Atm(object):

    #constructor
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber
        
    #start function
    def CashWithdrawl(self):
        print("Cash Withdrawl")
    
    #end function2
    def BalanceEnquiry(self):
        print("Balance Enquiry")


   


#object-main
atm=Atm("A6","904637")
print(atm.cardnumber)
print(atm.pinnumber)

atm.CashWithdrawl()
atm.BalanceEnquiry()
