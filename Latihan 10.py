#1
def printGreeting():
    print("Welcome to Our Website! Enjoy your visit!")
printGreeting()

#2
import random
def generateRandomNumber():
    print(random.randint(1, 100))
generateRandomNumber()

#3
def calculateArea():
    Length = 7
    Width = 5
    Area = Length * Width
    print("Luas nya adalah ", Area)
calculateArea()

#4
def calculateFactorial(n):
     factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

calculateFactorial()
