price_lookup = {
    'apple': 2.99,
    'banana': 1.50,
    'cherry': 3.0
}

print(price_lookup['cherry'])  # 3.0

new_dict = {
    'any': 1,
    'b': [1, 2, 3],
    'c': {"see": "you"}
}

print(new_dict['c']['see'])  # you
print(new_dict['b'][2])  # 3

# add new key:value oai to existing dict
new_dict['d'] = 3.14
print(new_dict)
# {'any': 1, 'b': [1, 2, 3], 'c': {'see': 'you'}, 'd': 3.14}
print(new_dict.keys())  # dict_keys(['any', 'b', 'c', 'd']) --> gets all keys
# dict_values([1, [1, 2, 3], {'see': 'you'}, 3.14])  --> gets all values
print(new_dict.values())
print(new_dict.get('any'))  # 1
