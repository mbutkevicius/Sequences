# for index, character in enumerate("abcdefgh"):
#     print(index, character)

# for t in enumerate("abcdefgh"):
#     print(t)

# this code is shorthand for lines 1-2. 8-10 show what's happening
for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)
