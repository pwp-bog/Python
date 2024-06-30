class calculator:
    def __init__(self, number1, operator, number2) -> None:
        self.num1, self.num2, self.op = int(number1), int(number2), operator
        result = 0
        if self.op == "minus":
            result = self.num1 - self.num2
        elif self.op == "plus":
            result = self.num1 + self.num2
        elif self.op == "multiply":
            result = self.num1 * self.num2
        else:
            if self.num1 == 0 or self.num2 == 0:
                result = None
            else:
                result = self.num1 / self.num2
        print(round(result))


n1, op, n2 = input().split(" ")
value = calculator(n1, op, n2)

