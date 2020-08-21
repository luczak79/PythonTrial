user1 = {
    'name': 'Sorna',
    'valid': True
}

user2 = {
    'name': 'Marcin',
    'valid': False
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
      print('Valid user: ' + args[0]['name'])
      fn(*args, **kwargs)
    else:
      print('Invalid user: ' + args[0]['name'])
      print('message has not been sent')
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

print('--------------')
message_friends(user1)
print('--------------')
message_friends(user2)
