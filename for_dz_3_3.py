marks = [{'school_class': '4a', 'scores': [3, 4, 5, 2, 4, 5, 2, 5]}, {'school_class': '4b', 'scores': [4, 5, 3, 4, 5, 4, 3, 4, 5]}, {'school_class': '4v', 'scores': [5, 5, 5, 5, 5]}]

# Задача 1 - Посчитать и вывести средний балл по всей школе
# Создаю переменную для прибавления в нее всех оценок по очереди
marks_sum = 0


# Добавляю счетчик, чтобы потом делить на него сумму оценок
count = 0


# Считаю и вывожу средний балл по всем классам
# Создаю цикл, который складывает все оценки в значениях обоих словарей
for dictionary in marks:
    for i in dictionary['scores']:
        # Суммирую оценки
        marks_sum += i
        # Считаю количество оценок
        count += 1


# Отображаю средний балл и округляю его до 2 знаков после точки
print('Средний балл по всей школе равен ' + str(round(marks_sum / count, 2)))



# Задача 2 - Посчитать и вывести средний балл по каждому классу
# Создаю схожий цикл "for" для подсчета среднего балла в каждом классе
for dictionary in marks:
    # обнуляю сумму и счетчик
    count = 0
    marks_sum = 0
    for i in dictionary['scores']:

        # Cнова суммирую оценки и считаю их количество
        marks_sum += i
        count += 1
    # Отображаю средний балл для каждого класса и округляю его до 2 знаков после точки
    print('Средний балл для класса ' + dictionary['school_class'] + ' равен ' + str(round(marks_sum / count, 2)))