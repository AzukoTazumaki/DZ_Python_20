from random import randint
import numpy as np


class Exercises:
    @staticmethod
    def ex_1() -> str:
        tuple_1 = tuple(randint(-50, 50) for _ in range(200))
        tuple_2 = tuple(randint(-50, 50) for _ in range(200))
        tuple_3 = tuple(randint(-50, 50) for _ in range(200))
        result = ', '.join(
            set(
                [str(x) for x in tuple_1 if x in tuple_2 and x in tuple_3]
            )
        )
        return result

    @staticmethod
    def ex_2() -> str:
        tuple_1 = tuple(randint(-50, 50) for _ in range(200))
        tuple_2 = tuple(randint(-50, 50) for _ in range(200))
        tuple_3 = tuple(randint(-50, 50) for _ in range(200))
        result = ', '.join(
            set(
                [str(x) for x in tuple_1 if x not in tuple_2 and x not in tuple_3] +
                [str(x) for x in tuple_2 if x not in tuple_1 and x not in tuple_2] +
                [str(x) for x in tuple_3 if x not in tuple_1 and x not in tuple_2]
            )
        )
        return result

    @staticmethod
    def ex_3() -> dict:
        tuple_1 = tuple(randint(-50, 50) for _ in range(200))
        tuple_2 = tuple(randint(-50, 50) for _ in range(200))
        tuple_3 = tuple(randint(-50, 50) for _ in range(200))
        result = dict()
        first_comparison = np.array(tuple_1) == np.array(tuple_2)
        result_comparison = first_comparison == np.array(tuple_3)
        for index, number in enumerate(result_comparison):
            if bool(number):
                result[index] = tuple_1[index]
        return result
