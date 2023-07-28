import math


def investment(amount, intRate, time):
    rate = intRate / 100
    interest = input("Investment Type: Simple/Compound Interest: \n").lower()
    print("****************************************************************************************************")

    if interest == "compound":
        total = float(amount * math.pow((1 + rate), time))
        print("Total interest after investment term is: R" + str("%.2f" % total))
        print("====================================================================================================")

    elif interest == "simple":
        total = float(amount * (1 + rate * time))
        print("Total interest after investment term is: R" + str("%.2f" % total))
        print("====================================================================================================")

    else:
        print("Invalid Input")


def bond(value, intRate, time):
    print("****************************************************************************************************")
    rate = (intRate/100) / 12
    repayment = (rate * value) / (1 - math.pow(1 + rate, (-1*time)))
    print("The amount to be repaid each month is: R" + str("%.2f" % repayment))
    print("====================================================================================================")


print("====================================================================================================")
print("-------------------------------------------Uncut Financial------------------------------------------")
print("****************************************************************************************************")
print("1.Investment        - To calculate the amount of interest you will earn on interest")
print("2.Bond              - To calculate the amount you'll have to pay on a home loan")
print("****************************************************************************************************")
respond = input("Choose either 'Investment' or 'Bond' from the below to proceed: \n").lower()

if respond == "investment":
    print("====================================================================================================")
    print("-----------------------------------------Uncut Investments------------------------------------------")
    print("****************************************************************************************************")
    input_rate = float(input("Enter interest rate (%): "))
    input_amount = float(input("Enter amount to be invested: R"))
    input_time = float(input("Enter number of years of investment: "))
    investment(input_amount, input_rate, input_time)
elif respond == "bond":
    print("====================================================================================================")
    print("-------------------------------------------Uncut Bonds----------------------------------------------")
    print("****************************************************************************************************")
    input_rate = int(input("Enter the annual interest rate (%): "))
    input_value = int(input("Enter current value of the property: R"))
    input_time = int(input("Enter number of MONTHS over which the bond will be paid: "))
    bond(input_value, input_rate, input_time)
else:
    print("Invalid input")
