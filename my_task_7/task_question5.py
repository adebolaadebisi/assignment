# task5
#Contact quick lookup
names = ('Bola', 'kemi', 'Friday')
phone_num = ('810067', '081699','905068' )
info = {name: num for name, num in zip(names, phone_num)}
new_name = input('Enter a name: ')
print(info.get(new_name))

