search_value = 12345
gist_dictionary = dict(id=12345,description='This is a demo gist')
#print(dir(gist_dictionary))

# Initialize a list to store keys where the value is found
keys_with_value = []

for key,value in gist_dictionary.items():
    print(f'Key:  {key}, Value: {value}')
    if value == search_value:
        keys_with_value.append(key)

if keys_with_value:
    print(f"The value '{search_value}' was found in the following key(s): {', '.join(keys_with_value)}")
else:
    print(f"The value '{search_value}' was not found in the dictionary.")

print(keys_with_value)