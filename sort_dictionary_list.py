dl = list()
d = dict()

d['name'] = 'Patrick'
d['age'] = 15
dl.append(d.copy())

d['name'] = 'John'
d['age'] = 32
dl.append(d.copy())

d['name'] = 'Max'
d['age'] = 19
dl.append(d.copy())

# Original list
print(dl)

# Sort by age
dl.sort(key=lambda x: x['age'])
print(dl)

# Sort by reversed age
dl.sort(key=lambda x: x['age'], reverse=True)
print(dl)

# Sort by name
dl.sort(key=lambda x: x['name'])
print(dl)
