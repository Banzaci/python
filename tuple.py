# Mix mellan string och array. Samma func som array men är imutable, som string. Array är mutable ie:

arr = [1,2,3]

arr[0] = 5

print(arr)


tupple = (1,2,3)

# tupple[0] = 5 - error

a,b,c = (1,2,3)

print(a,b,c)
# så list funktioner som .sort, .reverse och append finns ej på tupple då det göt ändringar.

# använder mindre minne, snabbare

# använd med listor som aldrig ska ändras

# error