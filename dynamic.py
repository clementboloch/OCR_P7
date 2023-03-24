from myDB import myDB
from timer import timer
from copy import deepcopy


def bestWay(names, prices, profits, budget, step):
    if len(prices) != len(profits):
        raise ValueError("The two lists must have the same length.")

    if (step == 0):
        return {'budget': budget, 'benefit': 0, 'list': deepcopy([])}

    price = prices[step - 1]

    if price > budget:
        return bestWay(names, prices, profits, budget, step - 1)
    else:
        profit = profits[step - 1]
        benefit = profit * price

        ifBuyChild = bestWay(names, prices, profits, budget - price, step - 1)
        ifBuyBenefit = benefit + ifBuyChild['benefit']
        ifBuyBudget = ifBuyChild['budget']
        ifLetChild = bestWay(names, prices, profits, budget, step - 1)
        ifLetBenefit = ifLetChild['benefit']
        ifLetBudget = ifLetChild['budget']
        if ifBuyBenefit >= ifLetBenefit:
            ifBuyList = ifBuyChild['list'] + [names[step - 1]]
            return {'budget': ifBuyBudget, 'benefit': ifBuyBenefit, 'list': ifBuyList}
        else:
            return {'budget': ifLetBudget, 'benefit': ifLetBenefit, 'list': ifLetChild['list']}


@timer
def getWay(path, budget, head=0):
    if head == 0:
        Data = myDB(path)
    else:
        Data = myDB(path, potential=True, head=head)
    names = Data.getColumn('name')
    prices = Data.getColumn('price')
    profits = Data.getColumn('profit')
    size = len(prices)
    return bestWay(names, prices, profits, budget, size)


results = getWay("data/data.xlsx", 500)
print(results)
