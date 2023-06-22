items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalon',
        'price': 120
    },
    {
        'product': 'chaqueta',
        'price': 200
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

# podriamos hacerlo asi
items_with_taxes = list(map(lambda item: {'product': item['product'], 'price': item['price'], 'tax_percent': 12, 'tax': item['price'] * 0.12, 'price_with_taxes': item['price'] * 1.12}, items))
print(items_with_taxes)

# sin embargo existe una manera mas elegante de hacerlo

def add_taxes(product):
    product['tax_percent'] = 12
    product['tax'] = product['price'] * .12
    product['price_with_taxes'] = product['price'] * 1.12
    return product


items_taxes = list(map(add_taxes, items))
print(items_taxes)