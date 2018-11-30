age = int(input('Введите, пожалуйста, ваш возраст: '))

def prof_orientation():
    answer = ''
    if age < 7:
        answer = 'Вам в сад.'
    elif age < 17:
        answer = 'Вам в шарагу.'
    elif age < 22:
        answer = 'Ваше место в вузе.'
    elif:
        answer = 'Вам на работу.'
    return answer

print(prof_orientation())
