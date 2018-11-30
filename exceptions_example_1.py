def cut_cake(parts):
    try:
        return 1/int(parts)
    except (ZeroDivisionError, TypeError, ValueError):
        return 'с ума посходили?'

print(cut_cake([1, 2]))