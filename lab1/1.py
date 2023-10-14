numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index = numbers.index(None)
first_part = numbers[:index]
second_part = numbers[index + 1:]
average = (sum(first_part) + sum(second_part)) / len(numbers)
numbers[index] = average
print("Измененный список:", numbers)
