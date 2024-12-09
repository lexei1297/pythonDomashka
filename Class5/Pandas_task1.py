import pandas as pd

def create_companyDF(income, expenses, years):
    """
    Создает DataFrame из списков доходов, расходов и годов.

    Args:
        income (list): Список доходов.
        expenses (list): Список расходов.
        years (list): Список годов.

    Returns:
        pd.DataFrame: DataFrame с доходами, расходами и годами в качестве индексов.
    """
    # Создаем DataFrame из входных данных
    data = {
        "Income": income,
        "Expenses": expenses
    }
    company_df = pd.DataFrame(data, index=years)

    # Переименовываем индекс
    company_df.index.name = "Year"

    return company_df


# Пример использования
income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]

company_df = create_companyDF(income, expenses, years)
print(company_df)