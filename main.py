import random
import sys
import math

class Calculator:
    def __init__(self, numbera, numberb):
        self.numbera = numbera
        self.numberb = numberb

    def __str__(self):
        return f"Calculate({self.numbera}, {self.numberb})"

    def __repr__(self):
        return self.__str__()

    def add(self):
        print(f"Adding two numbers {self.numbera} and {self.numberb}, the result is:")
        return self.numbera + self.numberb

    def sub(self):
        return self.numbera - self.numberb

    def mul(self):
        return self.numbera * self.numberb

    def div(self):
        if self.numberb == 0:
            return "Division by zero error"
        return self.numbera / self.numberb

    def power(self):
        return self.numbera ** self.numberb

    def mod(self):
        return self.numbera % self.numberb

    def floordiv(self):
        return self.numbera // self.numberb

    def sqroot(self):
        return math.sqrt(self.numbera), math.sqrt(self.numberb)

    def logarthm(self):
        return math.log(self.numbera), math.log(self.numberb)

    def factor(self):
        return math.factorial(self.numbera), math.factorial(self.numberb)

while True:
    # Display menu
    print("\n -- Calculator Menu -- ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponential")
    print("6. mod")
    print("7. Floordiv")
    print("8. Sqroot")
    print("9. logarithm")
    print("10. factoral")
    print("11. Exit")

    choice = input("Select an operation (1 to 11): ")

    if not choice.isdigit() or int(choice) not in range(1, 12):
        print("Invalid choice! Please enter a number between 1 and 11.")
        continue

    choice = int(choice)

    if choice == 11:
        print("Exiting calculator. Goodbye!")
        sys.exit()
        

    # Input numbers
    numbera = float(input("Enter numbera: "))
    numberb = float(input("Enter numberb: "))

    # Create calculator object
    cal1 = Calculator(numbera, numberb)
    print(cal1)
    

    # Perform chosen operation
    if choice == 1:
        print("Added:", cal1.add())
    elif choice == 2:
        print("Result:", cal1.sub())
    elif choice == 3:
        print("Result:", cal1.mul())
    elif choice == 4:
        print("Result:", cal1.div())
    elif choice == 5:
        print("Result:", cal1.power())
    elif choice == 6:
        print("Result:", cal1.mod())
    elif choice == 7:
        print("Result:", cal1.floordiv())
    elif choice == 8:
        print("Result:", cal1.sqroot())
    elif choice == 9:
        print("Result:", cal1.logarthm())
    elif choice == 10:
        print("Result:", cal1.factor())
