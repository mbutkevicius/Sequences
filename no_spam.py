menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
# This is his solution:
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))

# His second solution:
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=", ")
#     print()

# Second attempt works great but I don't think I was supposed to use while loop
# for meal in menu:
#     while "spam" in meal:
#         meal.remove("spam")
#     if "spam" not in meal:
#         print(meal)
#     else:
#         print(meal)

# My first attempt (works great but prints everything on same line)
# for meal in menu:
#     while "spam" in meal:
#         meal.remove("spam")
# print(menu)