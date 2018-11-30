dictionary = {"Как дела?": "Хорошо", "Что делаешь?": "Программирую"}

def ask_user():
    while True:
        ask_me = input('Задайте мне вопрос: ')
        if ask_me in dictionary:
            print(dictionary[ask_me])
        else:
            print('Я не знаю.')
            continue

ask_user()