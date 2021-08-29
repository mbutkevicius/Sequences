empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# numbers = even + odd
numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)



# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)      # to show that a new list was created with sorted()
#
# digits = list("432985617")  # creates list but doesn't sort it
# print(digits)       # produces list of str not int

# more_numbers = list(numbers)
# more_numbers = numbers[:]  # this sliced the list and created a new list
# more_numbers = numbers.copy()
# print(more_numbers)
# print(numbers is more_numbers)  # this shows it's a different list produced
# print(numbers == more_numbers)  # this shows that the two lists are equal

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
# # 'len' of a str would be character amount
# print(len(even))
# print(len(odd))
#
# print()
# print("Mississippi".count("issi"))
#
# even.extend(odd)
# print(even)
# another_even = even
# print(another_even)
#
# even.sort(reverse=True)
# print(even)