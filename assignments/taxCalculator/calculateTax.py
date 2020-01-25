#state=["Florida", "Texas","Arizona","NewYork"]
def netIncomeCalculator(state, grossIncome):
    statetax=0
    netIncome=0
    federalTax=10*grossIncome/100
    if state == "Florida":
        statetax=3*grossIncome/100
    elif state == "Texas":
        statetax=5*grossIncome/100
    elif state == "Arizona":
        statetax=7*grossIncome/100
    elif state is "NewYork":
       statetax=9*grossIncome/100
    else:
       print("No state tax")
        statetax=9*grossIncome/100
    netIncome=grossIncome-federalTax-statetax
    print("netIncome for state is " , str(netIncome))

#statename= input("Enter state name")
#income= input("Enter grossIncome")
z = netIncomeCalculator(statename,income)