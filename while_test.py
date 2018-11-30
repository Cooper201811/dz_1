while True:
    user_say = input('Скажите что-нибудь: ')
    if user_say == 'Пока':
        print('Ну пока')
        break
    else:
        print('Сам ты {}'.format(user_say))