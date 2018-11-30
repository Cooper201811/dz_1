def test_f(*args, **kwargs):
    print(args[0], args[1])
    print(kwargs['masha'], kwargs['petya'])
    return 0

test_f(1, 2, masha=165, petya=185)