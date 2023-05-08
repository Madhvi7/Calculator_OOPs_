"""create a class"""
class Calculator():
    """calculator class is created to perform basic calculations"""

    def __init__(self, num_1, num_2):
        self.num1 = num_1
        self.num2 = num_2

    def add(self):
        """Adding two numbers"""
        return self.num1 + self.num2


    def sub(self):
        """subtracting two numbers"""
        return self.num1 - self.num2

    def mul(self):
        """Multiplying two numbers"""
        return self.num1 * self.num2

    def divide(self):
        """dividing two numbers"""
        return self.num1 / self.num2


num1 = int(input('Enter First number'))
num2 = int(input('Enter Second number'))
obj = Calculator(num1, num2)
while True:

    print('1.Add \n2.Sub \n3. Mul \n4.Divide')

    choice = int(input('please select one of the following:'))
    if choice == 1:
        print("Result:", obj.add())

    elif choice == 2:
        print("Result:", obj.sub())

    elif choice == 3:
        print("Result:", obj.mul())

    elif choice == 4:
        print("Result:", obj.divide())

    elif choice == 0:
        print('Again try one of the following')


    else:
        print('invalid option')


print()
