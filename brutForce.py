import itertools
from copy import deepcopy
from myDB import myDB
from timer import timer


def buyOrNot(action, way):
    price = action['price']
    profit = action['profit']
    if price > way['budget']:
        return True
    else:
        way['budget'] -= action['price']
        way['benef'] += price * profit
        way['bought'].append(action['name'])
        return False


def defineBest(ways):
    best = {'budget': 0, 'benef': 0, 'bought': []}
    for way in ways:
        if way['benef'] > best['benef']:
            best = way
        elif (way['benef'] == best['benef']) & (way['budget'] > best['budget']):
            best = way
    return best


@timer
def getWay(path, budget, head=0, csv=False):
    if head == 0:
        Data = myDB(path, csv=csv)
    else:
        Data = myDB(path, potential=True, head=head, csv=csv)

    actions = list(Data.getDict().values())
    way_format = {'budget': budget, 'benef': 0, 'bought': []}
    ways = []
    combinations = list(itertools.permutations(range(Data.len())))

    for combination in combinations:
        way = deepcopy(way_format)
        for index in combination:
            stop = buyOrNot(actions[index], way)
            if stop:
                break
        ways.append(way)
    return defineBest(ways)


if __name__ == "__main__":
    best = getWay("data/data.xlsx", 500, 15)
    print(best)
