def greeting():
    print("Hi there!")
greeting()

def add_numbers(a, b):
    sum = a + b
    return sum

num1 = int(input(print("Masukan nilai pertama")))
num2 = int(input(print("Masukan nilai kedua")))
result = add_numbers(num1, num2)

print(f"The sum of {num1} and {num2} is: {result}")