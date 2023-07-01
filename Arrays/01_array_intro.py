def put_item_in_bag(item):
    # adding a item to bag list
    bag.append(item)


def print_items(item_list):
    print('index -> item')
    for i in range(len(item_list)):
        print(f'{i}    ->   {item_list[i]}')


# Creating Items list with values
items = ['egg', 'milk', 'yogurt', 'oil', 'bread', 'apples', 'bananas', 'chicken', 'rice', 'potatoes', 'tomatoes',
         'onions', 'carrots', 'lettuce', 'cheese']

# Creating bag list with empty values
bag = []

# Creating extra bag with empty values
extra_bag = list()

# Buying from the store
for item in items:
    put_item_in_bag(item)

print_items(bag)

dairy_products = ['milk', 'yogurt', 'cheese']
for i in range(len(bag)):
    if bag[i] in dairy_products:
        bag[i] = 'milk-product'

print('\nAfter modifying milk-products:\n', bag)

# insert into middle of the array
print('\nAdding curd to dairy products')
dairy_products.insert(1, 'curd')  # 2 arguments index and element
print_items(dairy_products)

# deleting from middle of the array
print('\nDeleting yogurt from dairy products')
dairy_products.remove('yogurt')
print_items(dairy_products)
