price = 100 # global scope

def increment():
    increment = price + 10 # local scope
    print(increment)
    return increment

print(price)
increment()