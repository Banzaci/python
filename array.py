arr = [1,2,3,4,5]
for a in arr:
  print(a)

print(arr[:3])
print(arr[3:])
print(arr[3:4])

newArr = [11,12,13]

con = arr + newArr

print(con)
con.append('Yoo')
print(con)

print(11 in con)
print(11 not in con)