file = open('my file.txt','r')


# content = file.readline()  # list 逐行 This is my first line.
allcontent = file.readlines()
# ['This is my first line.\n', 'This is my next line.\n', 'This is a appended file\n', 'This is a appended file']

print(allcontent)
