list = ['Minsk', 'Grodno', 'Brest', 'Vitebsk', 'Gomel']

user = 'o'

while user != 'q':
	user = input('''
q - quit
w - write
d - delete
p - print
	''')

	if user == 'w':
		i = input('Write: ')
		list.append(i)
	elif user == 'd':
		i = input('Delete index: ')
		del list[int(i)-1]
	elif user == 'p':
		for x in list:
			print (x)
