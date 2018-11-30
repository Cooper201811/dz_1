import random

def ask_user():
    while True:
        answer = input('Какой у вас еще вопрос? ')
        if answer == 'Пока!':
            print('Ну и отлично!')
            break
        else:
            print(get_answer)
            continue

def get_answer():
    bot_answer = random.choice(['Где карту заказывали, там и забирайте.', 'Галя, сделай отмену на кассе', 'Вам нужно заново взять справку по понедельникам в четные числа с 11:45 до 14:15'])
    return bot_answer


ask_user()
