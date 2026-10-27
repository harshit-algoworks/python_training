# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# d = int(input("Enter a number: "))

# if a > b and a > c and a > d:
#     print(f"{a} is the largest number")
# elif b > a and b > c and b > d:
#     print(f"{b} is the largest number")
# elif c > a and c > b and c > d:
#     print(f"{c} is the largest number")
# else:
#     print(f"{d} is the largest number")


# s = input("Enter a string: ")

# if "spam" in s or "eggs" in s or "bacon" in s:
#     print("Spam allert!!")
# else:
#     print(s)


j = input("Enter a name: ")

if len(j) == 10:
    print("Name perfect")
elif len(j) < 10:
    print("Name too short")
else:
    print("Name too long")