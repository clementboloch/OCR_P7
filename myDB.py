import pandas as pd


def str_to_float(val):
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


class myDB:
    def __init__(self, data, potential=False):
        self.df = pd.read_excel(data)
        self.columnsName = ['name', 'price', 'profit']
        self.cleanDB()
        if potential:
            self.calcPotential()

    def cleanDB(self):
        self.df.columns = self.columnsName
        for column in ['price', 'profit']:
            self.df[column] = self.df[column].apply(lambda x: str_to_float(x))

    def calcPotential(self):
        self.df['potential'] = self.df['profit'] / self.df['price']
        self.df.sort_values(by=['potential'])

    def getDict(self):
        return self.df.to_dict(orient='index')

    def getColumn(self, columnName):
        return self.df[columnName]
