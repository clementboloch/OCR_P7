from myDB import myDB

Data = myDB("data.xlsx", potential=True)
way = {'budget': 500, 'benef': 0, 'bought': []}


def buy(way, action):
    way['budget'] -= action['price']
    way['benef'] += action['price'] * action['profit']
    way['bought'].append(action['name'])


for index, action in Data.getDict().items():
    print('budget', way['budget'])
    buy(way, action)
    Data.rmAction(index)
    Data.rmExpensive(way['budget'])
    if Data.len() <= 0:
        break

print(way)
