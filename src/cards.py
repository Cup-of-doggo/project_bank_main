import pandas as pd


def get_cards(operations_df: pd.DataFrame) -> list[dict]:
    """Функция получения суммы расходов по картам"""
    df_expenses = operations_df[operations_df["Сумма платежа"] < 0]
    total_df = df_expenses[["Номер карты", "Сумма платежа", "Кэшбэк"]].groupby("Номер карты").sum().reset_index()
    total_df.rename(columns={"Номер карты": "last_digits", "Сумма платежа": "total_spent", "Кэшбэк": "cashback"},
    inplace=True)
    return total_df.to_dict(orient="records")
