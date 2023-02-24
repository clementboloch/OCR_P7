from data_to_dict import getColumn
from copy import deepcopy


prices = getColumn("data.xlsx", 'price')
profits = getColumn("data.xlsx", 'profit')
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
        ifBuy = benefit + bestWay(prices, profits, budget - price, step - 1)
        ifLet = bestWay(prices, profits, budget, step - 1)
        if ifBuy >= ifLet:
            return ifBuy
        else:
            return ifLet


def glob(prices, profits, budget, step):
    profit = bestWay(prices, profits, budget, step)
    return profit


print(len(glob(prices, profits, 500, size)))
