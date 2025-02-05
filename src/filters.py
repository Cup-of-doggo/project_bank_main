from src.file_reader import excel_reader


def top(dataframe):
    """возвращает топ 5 транзакций по сумме платежа"""
    sorted_df = dataframe.sort_values(by="Сумма операции")
    filtred_df = sorted_df.head(5)
    n = 0
    top_5 = []
    top_list = []
    top_5_data = []
    top_5_sum =[]
    top_5_cat = []
    top_5_des = []
    for data in filtred_df['Дата операции']:
        top_5_data.append(data)
    for sum in filtred_df['Сумма операции']:
        top_5_sum.append(sum)
    for cat in filtred_df['Категория']:
        top_5_cat.append(cat)
    for des in filtred_df['Описание']:
        top_5_des.append(des)
    top_list.append(top_5_data)
    top_list.append(top_5_sum)
    top_list.append(top_5_cat)
    top_list.append(top_5_des)
    for top in top_list:
        top_5.append({
            "date": top_5_data[n],
            "amount": top_5_sum[n],
            "category": top_5_cat[n],
            "description": top_5_des[n]
        })
        n += 1
    return top_5
