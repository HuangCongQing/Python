
try:
    file = open('eeeee', 'r+')
except Exception as e:
    print("[Errno 2] No such file or directory: 'eeeee'")
    response = input('do you want to create a new file?')
    if response == 'y':
        file = open('eeeee', 'w')
    else:
        pass
else:
    file.write('ssss')

