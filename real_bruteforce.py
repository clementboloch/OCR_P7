import itertools
from copy import deepcopy
from myDB import myDB


Data = myDB("data.xlsx")
actions = Data.getDict()
way_format = {'budget': 500, 'benef': 0, 'bought': []}
ways = []

size = 5
combinations = list(itertools.permutations(range(size)))


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


for combination in combinations:
    way = deepcopy(way_format)
    for index in combination:
        stop = buyOrNot(actions[index], way)
        if stop:
            break
    ways.append(way)

best = defineBest(ways)
print(best)
