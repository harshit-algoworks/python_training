d1 = {
    "harshit": 1,
    "harsh": 2,
    "harshita": 3,
    "hero" : 4
}

# print(d1["harshit"]) # prints the value of the key "harshit"
# print(d1.keys()) # prints all the keys of the dictionary
# print(d1.values()) # prints all the values of the dictionary
d1.update({"harshit": 5, "ballu" : 6}) # updates the value of the key "harshit" to 5
print(d1)

d1.pop("harsh") # removes the key "harsh" from the dictionary
print(d1)