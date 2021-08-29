
data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200
# It's fine code. Just seeing more examples
# for index in range(len(data) - 1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        # This gives the original index value since reversing
        # reverses index numbers. ie 108 is index position 0 before this
        print(top_index - index, value)
        del data[top_index - index]

print(data)
