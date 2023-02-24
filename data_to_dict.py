import pandas as pd

columnsName = ['name', 'price', 'profit']


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
    print(val)
    return val


def convert(data):
    df = pd.read_excel(data)
    df.columns = columnsName
    for column in ['price', 'profit']:
        df[column] = df[column].apply(lambda x: str_to_float(x))
    return df.to_dict(orient='index')
