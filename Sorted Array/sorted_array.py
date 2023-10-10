elements_in_array = int(input())
array = [int(ch) for ch in input().split(" ")]

for i in range(0, elements_in_array):
    if i == elements_in_array - 1:
        break
    if i % 2 == 0:
        if array[i] < array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    else:
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

print(*array)