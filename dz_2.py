def isstring(string_1, string_2):
    if type(string_1) != str or type(string_2) != str:
        return '0'
    # print(type(string_1), type(string_2))
    else:
        if string_1 == string_2:
            return '1'
        else:
            if string_1 != string_2 and len(string_1) > len(string_2):
                return '2'
            elif string_1 != string_2 and string_2 == 'learn':
                return '3'

result = isstring(string_1 = input('Напишите что-нибудь: '), string_2 = input('Напишите еще что-нибудь: '))
print(result)