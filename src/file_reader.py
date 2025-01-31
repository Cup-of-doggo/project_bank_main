import os
import pandas as pd


def excel_reader(filename):
    """преобразует эксель файл в обьект python"""
    filepath = os.path.join(os.path.dirname(__file__),"data",filename)
    data = pd.read_excel(filepath).to_dict('records')
    dataframe = pd.DataFrame(data=data)
    return dataframe
