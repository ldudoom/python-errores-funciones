# HOF -> High Order FUnction (funciones de orden superior)

def increment(x):
    return x + 1

def high_order_function(x, func):
    return x + func(x)

result = high_order_function(2, increment)
print(result)

# Ahora lo vamos a hacer usando lambdas

increment_v2 = lambda x: x + 1
high_order_function_v2 = lambda x, func: x + func(x)

result_v2 = high_order_function_v2(2, increment_v2)
print(result_v2)

print(high_order_function_v2(2, lambda x: x + 2))
print(high_order_function_v2(2, lambda x: x * 5))