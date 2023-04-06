list_of_sales = {}

for line in open('input.txt'):
    name, product, quantity = line.split()
    quantity = int(quantity)
    if name not in list_of_sales:
        list_of_sales[name] = {}
    if product not in list_of_sales[name]:
        list_of_sales[name][product] = 0
    list_of_sales[name][product] += quantity

for name, value in sorted(list_of_sales.items()):
    print(f'{name}:')
    for product, quantity in sorted(value.items()):
        print(product, quantity)
