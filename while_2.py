def find_person(find):

    mylist = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    name = ''
    while name != find:
        name = mylist.pop()
        print(mylist)
        if name == find:
            print(find + ' нашелся!')


find_person(find = input('Какое из этих имен вы хотите найти (Вася, Даша, Саша, Валера, Петя, Маша)? '))