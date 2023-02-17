import pandas as pd


def convert(data):
    excel_data_df = pd.read_excel(data)
    return excel_data_df.to_dict(orient='records')
