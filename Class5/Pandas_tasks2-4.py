# Задача 2.1: Цена объекта недвижимости под индексом 15
price_index_15 = melb_data.loc[15, 'Price']  # Предполагается, что есть столбец 'Price'
print(f"Цена объекта под индексом 15: {price_index_15}")

# Задача 2.2: Дата продажи объекта под индексом 90
sale_date_index_90 = melb_data.loc[90, 'Date']  # Предполагается, что есть столбец 'Date'
print(f"Объект под индексом 90 был продан: {sale_date_index_90}")

# Задача 3.1: Сколько объектов недвижимости без ванных комнат?
no_bathrooms_count = melb_data[melb_data['Bathroom'].isnull()].shape[0]  # Столбец 'Bathroom'
print(f"Число объектов без ванных комнат: {no_bathrooms_count}")

# Задача 3.2: Сколько объектов продал риелтор Nelson стоимостью более 3 млн?
nelson_sold_over_3m = melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3_000_000)].shape[
    0]  # 'SellerG' и 'Price'
print(f"Число объектов, проданных риелтором Nelson стоимостью более 3 млн: {nelson_sold_over_3m}")

#Задача 4: Функция удаления столбцов


def delete_columns(df, cols=[]):
    """
    Удаляет указанные столбцы из DataFrame.
    Если хотя бы одного столбца не существует, возвращает None.

    Args:
        df (pd.DataFrame): Исходный DataFrame.
        cols (list): Список столбцов для удаления.

    Returns:
        pd.DataFrame or None: Новый DataFrame или None, если хотя бы один столбец отсутствует.
    """
    # Проверяем, есть ли все указанные столбцы в DataFrame
    missing_cols = [col for col in cols if col not in df.columns]
    if missing_cols:
        print(f"Столбцы отсутствуют: {missing_cols}")
        return None

    # Удаляем указанные столбцы
    return df.drop(columns=cols)


# Пример использования
columns_to_delete = ['Column1', 'Column2']  # Укажите нужные столбцы
new_df = delete_columns(melb_data, columns_to_delete)
if new_df is not None:
    print("Обновленная таблица:")
    print(new_df.head())
else:
    print("Удаление не выполнено: указанных столбцов не существует.")