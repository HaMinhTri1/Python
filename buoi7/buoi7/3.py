def square(numbers):
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result
numbers = [1,2,3,4,5]
square_numbers = square(numbers)
print(square_numbers)