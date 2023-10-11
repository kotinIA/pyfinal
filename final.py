# Домашнее задание

# Чтобы перевести столбец 'whoAmI' в DataFrame в one-hot 
# кодирование без использования get_dummies, можно использовать 
# метод pd.get_dummies() 
# и затем объединить кодированные столбцы с исходным DataFrame. 
# Этот код создаст новые столбцы для каждого уникального значения 
# в столбце 'whoAmI' и закодирует значения как 0 и 1. 
# Результатом будет DataFrame без исходного столбца 'whoAmI', 
# а вместо него будут добавлены столбцы one-hot кодирования.

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
unique_values = data['whoAmI'].unique()

for value in unique_values:
    data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0)

data = data.drop('whoAmI', axis=1)
data.head()