numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_2 = numbers[:4] + numbers[5:]

sum_ = sum(numbers_2)
count = len(numbers)

numbers[4] = sum_ / count

print("Измененный список:", numbers)
