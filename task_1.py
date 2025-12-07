numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_ = sum(numbers[:4]) + sum(numbers[5:])
len_ = len(numbers)
numbers[4] = sum_/len_
print("Измененный список:", numbers)
