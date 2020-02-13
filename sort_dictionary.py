x = {'something': 'something', 'name': 'myName', 'last_name': 'my_last_name'}
print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])})  # Sort by value
print({k: v for k, v in sorted(x.items(), key=lambda item: item[0])})  # Sort by key
