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

def add_taxes(product):
    new_product = product.copy()
    new_product['tax_percent'] = 12
    new_product['tax'] = new_product['price'] * .12
    new_product['price_with_taxes'] = new_product['price'] * 1.12
    return new_product

items_taxes = list(map(add_taxes, items))
print('*' * 200)
print('New List')
print('*' * 200)
print(items_taxes)
print('*' * 200)
print('Old List')
print('*' * 200)
print(items)