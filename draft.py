from random import randint
import numpy as np

tuple_1 = tuple(randint(0, 30) for _ in range(200))
tuple_2 = tuple(randint(0, 30) for _ in range(200))
tuple_3 = tuple(randint(0, 30) for _ in range(200))
result = dict()

first_comparison = np.array(tuple_1) == np.array(tuple_2)
result_comparison = first_comparison == np.array(tuple_3)
for index, number in enumerate(result_comparison):
    if bool(number):
        result[index] = tuple_1[index]

for index, number in result.items():
    print(f'Индекс: {index}, Число: {number}')