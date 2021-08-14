import os

files = os.listdir('./')
try:
    os.mkdir('../extracted')
except:
    print('The folder has been created!!!')

for file in files:
    if file.split('.')[-1] == 'py':
        continue
    else:
        print('Excuting {}'.format(file))
        with open(file, 'r') as f:
            with open('../extracted/'+file, 'w') as p:
                count = 0
                for line in f.readlines():
                    if '>' == line[0]:
                        count += 1
                    if count == 3:
                        p.close()
                        break
                    p.write(line)
                f.close()
    
'''                
with open("./Valid name hits for D1-1.txt", "r") as f:
    data = f.readline()
    print(data)
'''