import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Задаём массив возможных значений для перемножения

answers = {'correct': 0, 'wrong': 0}    # Задаём словарь с счётчиками верных и неверных ответов (в начале работы равны нулю)

def multiplication(x, y):   # Определяем функцию принимающую на вход два числа
    result = input(f'{x} × {y} = ') # Запрашиваем результат перемножения двух чисел
    
    if (int(result) == x * y):  # Проверяем введённый пользователем результат с произведением
        print('Верно!')         # Выводим результат проверки ответа
        answers['correct'] += 1 # увеличиваем значение правильных ответов на единицу
    else:                                           # Если введённый ответ не совпадает с произведением
        print(f'Не верно! Правильный ответ: {x*y}') # Выводим сообщение с правильным ответом
        answers['wrong'] += 1                       # Увеличиваем счётчик неправильных ответов на единицу

game = True # Задаём переменную для начала игры

while game: # Пока переменная game является истиной продолжаем
    atempts = int(input('Введите количество примеров: '))   # Запрашиваем количество примеров у пользователя

    for i in range(atempts):    # Повторяем количество раз которое ввёл пользователь
        x = random.choice(nums) # Берём случайное значение из массива чисел для первого множителя
        y = random.choice(nums) # Берём случайное значение из массива чисел для второго множителя
        multiplication(x, y)    # Запускаем функцию с двумя случайными множителями
        
    game = 'д' != input('Закончить? (д/н): ')   # После окончания опроса, спрашиваем заканчивать или нет
print(f'Правильных ответов: {answers["correct"]}\nНеправильныйх ответов: {answers["wrong"]}')   # Выводим результат
input('Нажмите ENTER чтобы закрыть окно')   # Ожидаем завершения программы (чтобы окно само не закрылось после завершения)
