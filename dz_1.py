age = int(input('Введите, пожалуйста, ваш возраст: '))

def prof_orientation():
    if age < 7:
        print('Вам в сад.')
    elif 8 <= age < 17:
        print('Вам в шарагу.')
    elif 18 <= age < 22:
        print('Ваше место в вузе.')
    elif age >= 22:
        print('Вам на работу.')

prof_orientation()