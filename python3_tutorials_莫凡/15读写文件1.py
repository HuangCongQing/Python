text = "This is my first line.\nThis is my next line."
# print(text)

my_file = open('my file.txt', 'w')
my_file.write(text)
my_file.close()