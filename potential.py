from myDB import myDB
from timer import timer


def buy(way, action):
    way['budget'] -= action['price']
    way['benef'] += action['price'] * action['profit']
    way['bought'].append(action['name'])


@timer
def getWay(path, budget, csv=False):
    Data = myDB(path, potential=True, csv=csv)
    way = {'budget': budget, 'benef': 0, 'bought': []}

    for index, action in Data.getDict().items():
        # check if the dataframe contains row with index
        if index not in Data.df.index:
            continue
        buy(way, action)
        Data.rmAction(index)
        Data.rmExpensive(way['budget'])
        if Data.len() <= 0:
            break
    return way


if __name__ == "__main__":
    results = getWay("data/data.xlsx", 500)
    print(results)
