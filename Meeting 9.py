# # Example
# from array import array
# integer_array = array('i', [1, 2, 3, 4, 5])
# integer_array.append(3)

# integer_array[2] = 9
# integer_array[4] = 10

# integer_array.clear()
# print(integer_array)

from array import array

data = array('i')
for i in range(5):
    data.append(i * 10)

data[2] = 25
print("Array Values:")
for val in data:
    print(val, end=" ")

