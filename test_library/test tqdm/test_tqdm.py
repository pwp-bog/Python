a = "+"

num1 = int(input())
num2 = int(input())


def calc(a, num1, num2):
    """[calc]

    Args:
        a (str): [operathion]
        num1 (int): [first num]
        num2 (int): [second num]
    """

    if a == "+":
        print(num1 + num2)
    if a == "-":
        print(num1 - num2)
    if a == "*":
        print(num1 * num2)
    if a == "/":
        print(num1 / num2)


calc(a, num1, num2)
