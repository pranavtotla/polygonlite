def is_between(number1, number2, number3):
    if number2 >= number1:
        if number2 <= number3:
            return True
    elif number2 >= number3:
        if number1 <= number1:
            return True
    return False


dot = lambda X, Y: sum(map(lambda x, y: x * y, X, Y))
