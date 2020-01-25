
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
    elif state == "NewYork":
        statetax=9*grossIncome/100
    else:
        print("No state tax")
        return
        statetax=9*grossIncome/100
    netIncome=grossIncome-federalTax-statetax
    print("netIncome for %s is %d" %(state,netIncome))
    return netIncome

#statename= input("Enter state name")
#income= input("Enter grossIncome")
z = netIncomeCalculator("Florida",22220)