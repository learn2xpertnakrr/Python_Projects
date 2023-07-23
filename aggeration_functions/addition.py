def add(a, b):
    """Purpose :: To add the user given input numbers and return its sum"""
    print(a)
    print(b)
    d = a + b
    print(d)
    return d


def integer_test(a, b):
    if a >= 0 & b >= 0:
        print("both are integers")
        return True
    else:
        print("any one is non integer")
        return False


if __name__ == '__main__':
    print("----------Programs starts from this point--------")
    a = int(input("Please enter the first number ::"))
    b = int(input("Please enter the second number ::"))

    # Function call : Test entered numbers are integers or not
    test = integer_test(a, b)
    if test:
        pass
    else:
        print("Please enter only integers")
        exit(1)

    # Function call
    sum1 = add(a, b)
    print(f"addition of {a} and {b} = {sum1}")
