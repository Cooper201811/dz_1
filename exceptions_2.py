while True:
    try:
        def get_summ(num_one, num_two):
            return num_one + num_two

        print(get_summ(int(input('Введите первое число: ')), int(input('Введите второе число '))))
        break


    except (ValueError):
        print('Вам необходимо ввести числа, а не что-то другое.')