def check_even_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False


def divide_even(number):
    number = number / 2
    return number


def multiply_odd(number):
    number = number * 3 + 1
    return number


if __name__ == '__main__':
    num = int(input('Enter number: '))

    while num > 1:
        if check_even_odd(num):
            print(divide_even(num))
            num = divide_even(num)
        else:
            print(multiply_odd(num))
            num = multiply_odd(num)
