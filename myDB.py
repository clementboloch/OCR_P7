import pandas as pd


def cleanNum(val):
    if isinstance(val, (float, int)):
        return val
    val = val.replace(u'\xa0', u'')
    val = val.replace(u' ', u'')
    if '%' in val:
        val = val.replace(u'%', u'')
        val = float(val)
        val /= 100
    else:
        val = float(val)
    return val


def cleanAlpha(val):
    val = val.replace(u'\xa0', u'')
    val = val.replace(u' ', u'')
    return val


class myDB:
    def __init__(self, data, potential=False, head=0):
        self.df = pd.read_excel(data)
        self.columnsName = ['name', 'price', 'profit']
        self.cleanDB()
        if potential:
            self.calcPotential()
        if head:
            self.df = self.df.head(head)

    def cleanDB(self):
        self.df.columns = self.columnsName
        self.df.name = self.df.name.apply(lambda x: cleanAlpha(x))
        for column in ['price', 'profit']:
            self.df[column] = self.df[column].apply(lambda x: cleanNum(x))

    def calcPotential(self):
        self.df['potential'] = self.df['profit'] / self.df['price']
        self.df.sort_values(by=['potential'], ascending=False, inplace=True)

    def getDict(self):
        return self.df.to_dict(orient='index')

    def getColumn(self, columnName):
        return list(self.df[columnName])

    # Methods for potential algo
    def rmAction(self, index):
        self.df.drop(index, inplace=True)

    def rmExpensive(self, budget):
        self.df = self.df[self.df.price <= budget]

    def len(self):
        return len(self.df)
