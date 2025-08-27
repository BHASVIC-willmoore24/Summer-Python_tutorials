file = 'file.txt'

file = open(file, 'w') #write to file
file.write("test")

file.close()


file = 'file.txt'

file = open(file, 'r')
print(file.read())

file.close()
