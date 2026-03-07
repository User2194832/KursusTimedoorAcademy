i = 1
while i <= 5:
    print(i, end=" ")
    i += 1

j = 2
while j <= 10:
    print(j,end=" ")
    j += 3

password = "123456"

while True:
    input_password = input("Enter the Password:")
    if input_password == password:
        print("Access Granted")
        break
    else:
        print("Access Denied")

for i in range(10, 1, -2):
    print(i, end=" ")

while True:
    print("This is an infinite loop")