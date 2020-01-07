file = open('dbs/email.txt')

for line in file:
  line = line.rstrip()
  if line.startswith('From:'):
    print(len(line))
    print(line)