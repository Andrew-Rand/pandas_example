# Pandas example

Ядром pandas являются две структуры данных, в которых происходят все операции: ```Series``` и ```Dataframe```.
Особенности этих структур основаны на одной черте — интеграции в их структуру объектов index и labels (метки). С их помощью структурами становится очень легко манипулировать.

**Series** - это объект Pandas, который нужен для работы с одномерными данными.
Очень напоминает списки в Python, но имеет дополнительные возможности.
Одна из отличительных особенностей, что в Series операция применяется поэлементно,
а в list ко всему списку (some_list * 2)

Состоит из двух связанных между собой массивов:

1. Данные (данные любого типа NumPy)
2. index (метки)

**Dataframe** — это табличная структура данных, напоминающая таблицы из Excel. Ее главная задача — позволить использовать многомерные Series.
Dataframe состоит из упорядоченной коллекции колонок, каждая из которых содержит значение разных типов (числовое, строковое, булевое и так далее).

В отличие от Series у которого есть массив индексов с метками, ассоциированных с каждым из элементов, Dataframe имеет сразу два таких. 
Первый ассоциирован со строками (рядами) и напоминает таковой из Series. 
Каждая метка ассоциирована со всеми значениями в ряду. Второй содержит метки для каждой из колонок.
Dataframe можно воспринимать как dict, состоящий из Series, где ключи — названия колонок, а значения — объекты Series, которые формируют колонки самого объекта Dataframe. Наконец, все элементы в каждом объекте Series связаны в соответствии с массивом меток, называемым index.

## Datasets

### netflix_originals.csv

#### Context

This dataset consists of all Netflix original films released as of June 1st, 2021. Additionally, it also includes all Netflix documentaries and specials. The data was webscraped off of this Wikipedia page, which was then integrated with a dataset consisting of all of their corresponding IMDB scores. IMDB scores are voted on by community members, and the majority of the films have 1,000+ reviews.

#### Content

Included in the dataset is:

* Title of the film
* Genre of the film
* Original premiere date
* Runtime in minutes
* IMDB scores (as of 06/01/21)
* Languages currently available (as of 06/01/21)
* Acknowledgements
