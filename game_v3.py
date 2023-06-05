"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
   
    count = 0 # изначальное значение счетчика
    max_point = 101 # определяем максимальное значение числа +1
    min_point = 0  # определяем минимальное значение
    
    while True:   # используем бесконечный цикл
      count += 1
      predict=(max_point+min_point)//2 #сокращаем возможные варианты в 2 раза, в зависимости от области нахождения числа
      if predict==number:
        break # выход из цикла если угадали
      elif predict<number: # при получении значения меньшего  или большего от загаданного числа сдвигаем границы 
        min_point=predict
      else:
        max_point=predict
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
