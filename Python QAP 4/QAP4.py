# comments a plenty
# Name: Evan Kavanagh
# Date: July 19th, 2024 - July 25th, 2024
# About: A program that creates receipts for the One Stop Insurance Company
#        and also keeps track of the Claims of customers. Utilizes a Const.dat
#        file and a Claims.dat file to do things easier, and has a loading bar.

import datetime
import sys
import time

# Define program functions.
def constOpen():
    f = open("QAP 4\Const.dat", "r")
    constRead = f.readlines()
    f.close()
    return constRead

def writeClaim(claimdata, file):
    f = open(file, 'a')
    f.write(f"{claimdata}\n")

# loading bar
def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

def clearClaims(file):
    open(file, 'w').close()

def readClaims(file):
    with open(file, 'r') as f:
        claims = f.readlines()
    return claims

# the function responsible for creating the claim receipt at the end
def printReceipt(claims):
    print(f"Claim #     Claim Date:     Amount")
    print(f"----------------------------------")
    for claim in claims:
        claimNum, claimDate, claimCost = claim.strip().split(", ")
        print(f"{claimNum:<7s}    {claimDate:<10s}  ${float(claimCost):>10,.2f}")
    print(f"----------------------------------")

#  define constants, mainly using the Const.dat file

TODAY_DATE = datetime.date.today()

constRead = constOpen()
POLICY_NUMBER = int(constRead[0].strip())
BASIC_PREMIUM = float(constRead[1].strip())
AUTO_DISCOUNT = float(constRead[2].strip())
EXTRA_LIAB_COVERAGE = float(constRead[3].strip())
GLASS_COVERAGE = float(constRead[4].strip())
LOAN_CAR_COVERAGE = float(constRead[5].strip())
HST_RATE = float(constRead[6].strip())
MONTHLY_FEES = float(constRead[7].strip())
NO_ADD_FEE = float(constRead[8].strip())

#gather user inputs

# constantly loops until end is inputted
# upon being requested to end, the program will ask if the user wants to save the changes made in Claims.dat
# yes will just end the program, no will erase the Claims.dat file alongside closing the program
while True:
    custFirst = input("Please enter the customer's first name (or enter 'End' to end program): ").title()
    if custFirst == "End":
        while True:
            clearConfirm = input("Do you wish to save changes to Claims.dat? (Y/N): ")
            if clearConfirm == "Y":
                    print("Thank you for using this program! Have a great day!")
                    exit()
            elif clearConfirm == "N":
                clearClaims("QAP 4/Claims.dat")
                print("Thank you for using this program! Have a great day!")
                exit()
            else:
                print()
                print("Oops! An error has occurred!")
                print("Error: invalid variable. Please try again!")
                print()

    custLast = input("Enter the customer's last name: ").title()
    custAdd = input("Enter the customer's address: ").title()
    custCity = input("Enter the customer's city: ").title()

    # validates the province
    provList = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YK"]
    while True:
        custProv = input("Enter the customer's province: ").upper()
        if custProv in provList:
            break
        else:
            print()
            print("Oops! An error has occurred!")
            print("Error: invalid variable. Please try again!")
            print()

    custPost = input("Enter the customer's postal code (X0X0X0): ").upper()
    phoneNum = input("Enter the customer's phone number (XXXXXXXXXX): ")
    carInsure = int(input("Enter the number of cars insured: "))

    # if yes, will add EXTRA_LIAB_COVERAGE, which is 130.00 according to the Const.dat file.
    # otherwise will be 0, thanks to the NO_ADD_FEE constant.
    while True:
        extraLiab = input("Does the customer want extra liability? (Y/N): ").upper()
        if extraLiab == "Y":
            liabFee = EXTRA_LIAB_COVERAGE
            break
        elif extraLiab == "N":
            liabFee = NO_ADD_FEE
            break
        else:
            print()
            print("Oops! An error has occurred!")
            print("Error: invalid variable. Please try again!")
            print()

    # if yes, will add GLASS_COVERAGE, which is 86.00 according to the Const.dat file.
    # otherwise will be 0, thanks to the NO_ADD_FEE constant.
    while True:
        optGlass = input("Does the customer want glass coverage? (Y/N): ").upper()
        if optGlass == "Y":
            glassFee = GLASS_COVERAGE
            break
        elif optGlass == "N":
            glassFee = NO_ADD_FEE
            break
        else:
            print()
            print("Oops! An error has occurred!")
            print("Error: invalid variable. Please try again!")
            print()

    # if yes, will add LOAN_CAR_COVERAGE, which is 58.00 according to the Const.dat file.
    # otherwise will be 0, thanks to the NO_ADD_FEE constant.
    while True:
        optLoanCar = input("Does the customer want an optional loaner car? (Y/N): ").upper()
        if optLoanCar == "Y":
            loanFee = LOAN_CAR_COVERAGE
            break
        elif optLoanCar == "N":
            loanFee = NO_ADD_FEE
            break
        else:
            print()
            print("Oops! An error has occurred!")
            print("Error: invalid variable. Please try again!")
            print()

    # ignores monthFee and downPay if full is selected
    # adds the MONTHLY_FEE constant if monthly is selected
    # adds the MONTHLY_FEE constant and asks the user to input a Down Payment amount if down pay is selected
    payList = ["Full", "Monthly", "Down Pay"]
    while True:
        payMethod = input("How is the customer paying? (Full/Monthly/Down Pay): ").title()
        if payMethod in payList:
            if payMethod == "Full":
                monthFee = NO_ADD_FEE
                downPay = NO_ADD_FEE
                break
            elif payMethod == "Monthly":
                monthFee = MONTHLY_FEES
                downPay = NO_ADD_FEE
                break
            else:
                monthFee = MONTHLY_FEES
                downPay = float(input("Please enter the customer's down payment amount: "))
                break
        else:
            print()
            print("Oops! An error has occurred!")
            print("Error: invalid variable. Please try again!")
            print()

    # these will be used in the claims receipt at the end
    claimNum = input("Enter the claim number: ")
    claimDate = input("Enter the claim date (MM-DD-YYYY): ")
    claimCost = input("Enter the claim cost: ")

    claimdata = f"{str(claimNum)}, {str(claimDate)}, {str(claimCost)}"
    writeClaim(claimdata, "QAP 4\Claims.dat")
    print("Claim data successfully saved.")


    # simple calculation that gives a discound if the customer has more than 1 car insured.
    if carInsure > 1:
        autoCost = BASIC_PREMIUM + (BASIC_PREMIUM * (carInsure - 1) * (1 - AUTO_DISCOUNT))
    else:
        autoCost = BASIC_PREMIUM
    extraCost = (liabFee + glassFee + loanFee) * carInsure
    totPremium = autoCost + extraCost

    # depending on the payMethod, insureCost will change accordingly
    if payMethod == "Monthly":
        insureCost = (totPremium + monthFee) / 8
    elif payMethod == "Down Pay":
        insureCost = ((totPremium - downPay) + monthFee) / 8
    else:
        insureCost = totPremium + monthFee

    costHST = insureCost * HST_RATE
    totCost = totPremium + costHST

    # moves the date ahead a year if it is december, making firstPayDate January 1st, YYYY.
    # otherwise, the firstPayDate will be the first day of next month with no year change.
    invoiceDate = datetime.date.today()
    if invoiceDate.month == 12:
        firstPayDate = invoiceDate.replace(year=invoiceDate.year + 1, month=1, day=1)
    else:
        firstPayDate = invoiceDate.replace(month=invoiceDate.month + 1, day=1)


    # required formatting (time-based)
    invoiceDateDsp = invoiceDate.strftime("%B %d, %Y")
    firstPayDateDsp = firstPayDate.strftime("%B %d, %Y")

    # required formatting (customer information-based)
    custNameDsp = f"{custFirst} {custLast}"
    custPostDsp = f"{custPost[0:3]} {custPost[3:6]}"
    phoneNumDsp = f"({phoneNum[0:3]}) {phoneNum[3:6]}-{phoneNum[6:10]}"

    # required formatting (money-based)
    downPayDsp = "${:,.2f}".format(downPay)
    liabFeeDsp = "${:,.2f}".format(liabFee)
    glassFeeDsp = "${:,.2f}".format(glassFee)
    loanFeeDsp = "${:,.2f}".format(loanFee)
    autoCostDsp = "${:,.2f}".format(autoCost)
    extraCostDsp = "${:,.2f}".format(extraCost)
    totPremiumDsp = "${:,.2f}".format(totPremium)
    costHSTDsp = "${:,.2f}".format(costHST)
    totCostDsp = "${:,.2f}".format(totCost)
    insureCostDsp = "${:,.2f}".format(insureCost)

    print(f"--------------------------------------------------------------------------")
    print(f"                        One Stop Insurance Company                        ")
    print(f"--------------------------------------------------------------------------")
    print(f"{custNameDsp:<30s}    Invoice Date:         {invoiceDateDsp:>18s}")
    print(f"{custAdd:<30s}")
    print(f"{custCity}, {custProv}, {custPostDsp}")
    print(f"{phoneNumDsp:<14s}                    Vehicle(s) insured:                   {carInsure:>2}")
    print(f"                                  Payment method:                 {payMethod:>8s}")

    # the receipt changes to include the down payment if the payMethod is Down Pay.
    # otherwise, the receipt won't include down payment.
    if payMethod == "Down Pay":
        print(f"|       Additional options:      |Down payment:                -{downPayDsp:>10s}")
    else:
        print(f"|       Additional options:      |")

    print(f"|Optional liability:     {liabFeeDsp:>3s} |----------------------------------------")
    print(f"|Optional glass coverage: {glassFeeDsp:>3s} |Insurance premiums:           {autoCostDsp:>10s}")
    print(f"|Optional loaner car:     {loanFeeDsp:>3s} |Extra costs charges:          {extraCostDsp:>10s}")
    print(f"                                  ----------------------------------------")
    print(f"                                  Sub-total:                    {totPremiumDsp:>10s}")
    print(f"                                  Taxes:                        {costHSTDsp:>10s}")
    print(f"                                  ----------------------------------------")
    print(f"                                  Total Due:                    {totCostDsp:>10s}")
    print(f"--------------------------------------------------------------------------")

    # this part at the end only happens if the customer's payMethod is down pay or monthly.
    # it informs the customer of the cost of their monthly payment and the date they are expected to pay.
    if payMethod == "Down Pay" or payMethod == "Monthly":
        print(f"               Next Expected Monthly Payment: {insureCostDsp:>10s}")
        print(f"                      Due Date: {firstPayDateDsp:>18s}")
        print(f"--------------------------------------------------------------------------")
    print(f"")
    print(f"")
    print(f"")

    # the loading bar in action
    TotalIterations = 30
    Message = "Saving Data..."
    for i in range(TotalIterations + 1):
        time.sleep(0.1)
        ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)

    print(f"")
    print(f"")
    print(f"")

    # creates a receipt using all the information stored in Claims.dat
    claims = readClaims("QAP 4/Claims.dat")
    printReceipt(claims)

    print(f"")
    print(f"Repeating program...")
    print(f"")