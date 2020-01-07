# x = 0

# while x < 10:
#   print(x)
#   x = x + 1


# x = int(input('Enter a number: '))

# if x < 0:
#   x = 0
#   print('Negative')
# elif x == 0:
#   print('Zero')
# else:
#   print('Positive')

# pets = ['dog', 'cat', 'mouse']

# for pet in pets:
#   print('I have a {0}'.format(pet))

# for i in range(10, 0, -1):
#   print(i)

# def get_sum(args):
#   print(*args)

# def main():
#   return get_sum

# if __name__ == '__main__':
#   args = [1, 2, 3]
#   func = main()
#   func(args)

def my_decorator(f):
  def wrapper(*args, **kwargs):
    res = f(*args, **kwargs)
    if isinstance(res, dict):
      print('-------')
      print(args)
      print(kwargs)
      return res
  return wrapper

@my_decorator
def my_code(args):
    return { 'lang': args }

print(my_code([1,2,3]))