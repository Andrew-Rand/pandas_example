import pandas as pd

# Чтение из csv файла
netflix_data = pd.read_csv("datasets/netflix_originals.csv", encoding="windows-1251")
# Также можно читать Excel
# netflix_excel = pd.read_excel("netflix.xlsx", sheet_name="Films")

# Deep copy данных
netflix = netflix_data.copy(deep=True)

# Вывод DataFrame в консоль
print(netflix)

print(f"Статистические сведений о DataFrame:\n", netflix.describe())

print(f"Всего строк в DataFrame: {len(netflix)}")
print(f"Строк и столбцов в DataFrame: {netflix.shape}")

print(f"Первые 5 строк:\n", netflix.head())
print(f"Первые 3 строки:\n", netflix.head(3))

print(f"Последние 5 строк:\n", netflix.tail())
print(f"Последние 3 строки:\n", netflix.tail(3))

print(f"Случайная строка:\n", netflix.sample())
print(f"Случайные 3 строки:\n", netflix.sample(3))

print("Информация о DataFrame:\n", netflix.info())

# Подсчёт количества уникальных значений в столбце
print(f"Количество представленных языков: {len(netflix['Language'].unique())}")

# Подсчёт количества значений
print(f"Количество фильмов в разрезе по языкам:\n", netflix["Language"].value_counts())

# Список значений столбцов
print(f"Столбцы: {netflix.columns.tolist()}")

print(f"Объект индекса: {netflix.index}")

# Получение списка значений из индекса
print(f"Значения индекса: {netflix.index.tolist()}")

print(f"Значения колонки Language: {netflix['Language'].tolist()}")
# Можно обратиться и по атрибуту
# netflix.Language.tolist()

# Присоединение к DataFrame нового столбца с заданным значением
netflix['train_set'] = True

# Тип object — это текст, float64 — это дробное число типа 3,14.
print(f"Типы столбцов:\n", netflix.dtypes)

print(f"Все ли названия фильмов уникальны: {netflix.Title.is_unique}")

# Создание нового датафрейма из подмножества столбцов
# anime[['name','episodes']]

# Удаление заданных столбцов
print(f"Удалили 2 столбца:\n", netflix.drop(["Runtime", "train_set"], axis=1).head())

# Для удаления целой колонки также можно воспользоваться del
# del netflix['Runtime']

print(f"Группировка по столбцу:\n", netflix.groupby("Genre").count())


# Выбор строки по метке	dataframe.loc[label]
# Выбор строки по индексу dataframe.iloc[loc]
filter_up_8 = netflix["IMDB Score"] > 8
print(
    f"Фильмы с рейтингом больше 8:\n",
    netflix.loc[filter_up_8].sort_values(by="IMDB Score", ascending=False)
)

runtime_more_than_90 = netflix["Runtime"] > 90
print(
    f"Фильмы с рейтингом больше 8 и длиной больше 90:\n",
    netflix.loc[filter_up_8][runtime_more_than_90].sort_values(by="IMDB Score", ascending=False)
)

print("Рейтинговые документалки:\n", netflix.query("Runtime > 90 & Genre == 'Documentary'"))


# также можно использовать переменные
# runtime_filter = 90
# genre_filter = 'Documentary'
# netflix.query("Runtime > @runtime_filter & Genre == @genre_filter"


# Транспонирование Dataframe
# При работе с табличным структурами данных иногда появляется необходимость
# выполнить операцию перестановки (сделать так, чтобы колонки стали рядами и наоборот).
# pandas позволяет добиться этого очень просто. Достаточно добавить атрибут T.
# netflix.T

# Экспорт в csv
# netflix[:10].to_csv('saved_netflix.csv', index=False)
