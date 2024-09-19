# # # for x in range (0, 10000):
# # #     print(x)

# # my_names = ["josh", "Jojo", "daniel"]

# # for x in my_names:
# #     if x.startswith("j"):
# #         print(x)


# # def josh():
# #     print(x)

# def Increment(number,by):
#     return number * by


# x = Increment(number=3,by=6 )
# print(x)

# multo

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)

user_input = input("Please enter a number: ")

# Convert the input to an integer
try:
    user_number = int(user_input)
    fizzbuzz(user_number)
except ValueError:
    print("Please enter a valid integer.")
