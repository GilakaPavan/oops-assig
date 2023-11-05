# Challenge1
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqsum(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2
point = Point(1, 3, 5)
result = point.sqsum()
print(result)
#---------------
#challenge2 
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num1 == 0:
            return "Division by zero is not allowed"
        return self.num2 / self.num1
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num1 == 0:
            return "Division by zero is not allowed"
        return self.num2 / self.num1
obj = Calculator(10, 94)
result_add = obj.add()
result_subtract = obj.subtract()
result_multiply = obj.multiply()
result_divide = obj.divide()

print(result_add)
print(result_subtract)
print(result_multiply)
print(result_divide) 
#------------------------------
#challenge 3
class Student:
    def __init__(self):
        self._name = None
        self._rollNumber = None

    # Getter for name
    def getName(self):
        return self._name

    # Setter for name
    def setName(self, name):
        self._name = name

    # Getter for rollNumber
    def getRollNumber(self):
        return self._rollNumber

    # Setter for rollNumber
    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber

student = Student()
student.setName("John")
student.setRollNumber(12345)

print(student.getName())
print(student.getRollNumber())
#------------------------------------------------------------------------------------------------------------------------------------------
# challenge 4 
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

# Usage
account1 = Account("Ashish", 5000)
savings_account1 = SavingsAccount("Ashish", 5000, 5)

print(account1.title) 
print(account1.balance)        

print(savings_account1.title)  
print(savings_account1.balance)  
print(savings_account1.interestRate)

#-------------------------------------------------------------------
#challenge 5 
class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100

# Code to test
savings_account = SavingsAccount("Ashish", 2000, 5) 

savings_account.deposit(500) 
savings_account.withdrawal(200) 

print(savings_account.getBalance()) 

interest = savings_account.interestAmount()
print(interest) 