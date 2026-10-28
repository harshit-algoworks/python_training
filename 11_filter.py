l = [1, 2, 3, 4, 5]

def check(num):
    if num > 3:
        return num 

result = list(filter(check, l)) 
print(result) # prints the even numbers in the list l