mylist = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
name = 'Глеб'
while name != 'Валера':
    name = mylist.pop()
    print(mylist)
    if name == 'Валера':
        print('Валера нашелся!')