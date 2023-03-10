from myDB import myDB
from copy import deepcopy

# Data = myDB("data.xlsx")
Data = myDB("data.xlsx", potential=True, head=17)
prices = Data.getColumn('price')
profits = Data.getColumn('profit')
size = len(prices)


def bestWay(prices, profits, budget, step):
    if len(prices) != len(profits):
        raise ValueError("The two lists must have the same length.")

    if (step == 0):
        return {'benefit': 0, 'list': deepcopy([])}

    price = prices[step - 1]

    if price > budget:
        return bestWay(prices, profits, budget, step - 1)
    else:
        profit = profits[step - 1]
        benefit = profit * price

        ifBuyChild = bestWay(prices, profits, budget - price, step - 1)
        ifBuyBenefit = benefit + ifBuyChild['benefit']
        ifLetChild = bestWay(prices, profits, budget, step - 1)
        ifLetBenefit = ifLetChild['benefit']
        if ifBuyBenefit >= ifLetBenefit:
            ifBuyList = ifBuyChild['list'] + [step - 1]
            return {'benefit': ifBuyBenefit, 'list': ifBuyList}
        else:
            return {'benefit': ifLetBenefit, 'list': ifLetChild['list']}


results = bestWay(prices, profits, 500, size)
print(results)
