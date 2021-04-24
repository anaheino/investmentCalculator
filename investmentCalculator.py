#!/usr/bin/python3
import sys


def calculateInvestments(investmentsPerYear, years, gainAsNumber, calcOnlyWholeSum):
    i = 0
    wholeSum = investmentsPerYear if calcOnlyWholeSum else 0
    while i < years:
        if calcOnlyWholeSum:
            wholeSum = wholeSum * gainAsNumber
        else:	
            wholeSum = (wholeSum + investmentsPerYear) * gainAsNumber
        i+=1
    return wholeSum


if __name__ == "__main__":
    print("Monetary value after this time would be:")
    n = 3
    investmentsPerYear = sys.argv[1]
    years = sys.argv[2]
    gainAsNumber = sys.argv[3] if len(sys.argv) > 3 else 1
    calcOnlyWholeSum = True if len(sys.argv) > 4 else False

    moneyArray = str(calculateInvestments(int(investmentsPerYear), int(years), float(gainAsNumber), calcOnlyWholeSum)).split(".")
    sumOfMoney = moneyArray[0][::-1]
    formatted = [sumOfMoney[index : index + n] for index in range(0, len(sumOfMoney), n)]
    print(" ".join(formatted)[::-1]+","+str(moneyArray[1])[0: 2])
