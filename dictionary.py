d = dict({ 'name': 'apa' })

# d['name'] = 'Miche'
# print(d)

# for (k,v) in d.items():
#   print(k,v)


d1 = { 'a': 1, 'c': 3, 'b': 2 }

t1 = sorted(d1.items())

# print(t1)

file = open('dbs/words.txt')

arr = dict()

for line in file:
  words = line.split()
  for word in words:
    arr[word] = arr.get(word, 0) + 1

lst = list()
for key, value in arr.items():
  lst.append((value, key))

lst.sort(reverse=True)

for key, value in lst[:10]:
  # print(key, value)
  pass
  # SHorter version


arr1 = sorted([( value, key ) for key, value in arr.items()])

test = dict({ 'word': '', 'count': 0 })

for key, value in arr1:
  if key > test['count']:
    test['count'], test['word'] = key, value

print(test)

# print(lst)