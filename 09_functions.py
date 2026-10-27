i = 1


def func (*val): # * is used to pass a variable number of arguments to a function. It allows you to pass any number of positional arguments to the function, which are then collected into a tuple named val.
    print(val)

func(1, 2, 3, 4, 35)


l = [1, 2, 3, 4, 5]
def square(num):
    return num * num

result = list(map(square, l))
print(result) # prints the square of each number in the list l