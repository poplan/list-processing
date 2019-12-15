import duplicate as dup

list = ['Minsk', 'Grodno', 'Brest', 'Vitebsk', 'Gomel', 'Gomel']

user = 'o'

while user != 'q':
	user = input('''
q - quit
w - write
d - delete
p - print
x - check duplicate
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
	elif user == 'x':
		result = dup.checkIfDuplicates_1(list)
		if result:
			print('Yes, list contains duplicates')
		else:
			print('No duplicates found in list')   
		


