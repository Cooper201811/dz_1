def ask_user():
    while True:
        answer = input('Как дела? ')
        if answer == 'Хорошо':
            print('Ну и отлично!')
            break
        else:
            continue

ask_user()