"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
# Импортируем библиотеку для генерации случайных чисел
import numpy as np 

def game_core_v3(number) -> int:

    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    pr_min = 1
    pr_max = 101
   
    count = 1  # количество попыток
    # предполагаемое число выбирает компьютер от 1 до 101
    predict_number = np.random.randint(1, 101)  
    while number != predict_number:
       
        if (pr_max - pr_min) < 2:
            break 
        count += 1
       

        if predict_number > number:  # если предсказанное число больше задуманного
            pr_max = predict_number
            predict_number = round((pr_min+pr_max)/2)
        
        else:
            # если предсказанное число меньше задуманного
            pr_min = predict_number
            predict_number = round((pr_min + pr_max) / 2)
   
    return count # возвращаем число попыток

# Функция для определения числа попыток, за которое программа угадывает число.
def score_game(game_core_v3) -> int:

    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел
   
    for number in random_array:
        count_ls.append(game_core_v3(number))
        score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


score_game(game_core_v3)
