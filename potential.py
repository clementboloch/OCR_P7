from myDB import myDB
from timer import timer


def buy(way, action):
    way['budget'] -= action['price']
    way['benef'] += action['price'] * action['profit']
    way['bought'].append(action['name'])


@timer
def getWay(path, budget):
    Data = myDB(path, potential=True)
    way = {'budget': budget, 'benef': 0, 'bought': []}

    for index, action in Data.getDict().items():
        buy(way, action)
        Data.rmAction(index)
        Data.rmExpensive(way['budget'])
        if Data.len() <= 0:
            break
    return way


results = getWay("data/data.xlsx", 500)
print(results)
