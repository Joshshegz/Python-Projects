# my_list = [2, 3, 5, 6, 92, 4, 5 ]


# first, numbers, *others = my_list
# print(others)

# list = ["a", "b", "c"]

# for index, letters in enumerate(list):
#     print(index, letters)

#Adding and removing items
# list = ["a", "b", "c"]

# list.append("d")
# print(list)

# list.insert(0, 34)

# print(list)


# price_item = [
#     ("milk", 200),
#     ("sugar", 500),
#     ("coke", 100),
# ]

# #using a lambda function
# price_item. sort(key=lambda item: item[1])
# print(price_item)

# #map functions
# x = list(map(lambda item:item[1], price_item ))
# print(x)

#list comprehensions

#SHORT EXERCISE
from pprint import pprint
sentence = "This is a common interview question"

char_count = {}
for char in sentence:
    if char in char_count:
        char_count[char]    += 1
    else:
        char_count[char] = 1
pprint (char_count, width=1)


print(sorted(char_count.items(), key=lambda item: item[1]))
