def isstring(string_1, string_2):
    if not (isinstance(string_1, str) and isinstance(string_2, str)):
        return '0'
    # print(type(string_1), type(string_2))
    elif string_1 == string_2:
        return '1'
    elif len(string_1) > len(string_2):
        return '2'
    elif string_2 == 'learn':
        return '3'


string_1, string_2 = input('Напишите что-нибудь: '), input('Напишите еще что-нибудь: ')
result = isstring(string_1, string_2)
print(result)
