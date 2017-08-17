# -*- coding: UTF-8 -*-
'''
Created on 2017年8月16日

@author: hasee
'''
# 读取csv文件
#     reader(csvfile, dialect='excel', **fmtparams)
#   写csv元件  
    # writer(csvfile, dialect='excel', **fmtparams)

# import csv
# with open('测试数据.csv','rt') as csv_file:
#     csv_conent = [ row for row in csv.reader(csv_file)]
#     print(csv_conent)

    # class csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
    # 可以使用DicReader()按照字典的方式读取csv内容
#     
# import csv
# with open('测试数据.csv','rt',newline='') as csvfile:
#     reader = csv.DictReader(csvfile, fieldnames =[1,2],delimiter=':')
#     for row in reader:
#         print(row[1],row[2])




# 2，写入csv文件   csv.writer(csvfile, dialect='excel', **fmtparams)
# 使用writer()函数来写csv文件，返回一个writer对象。writer对象可以使用writerow()写一行数据，或者使用writerows()写多行数据
# import csv
# namelist = []
# namelist = [
# ['Doctor','No'],
# ['Rosa','Klebb'],
# ['Mister','Big'],
# ['Auric','Gold'],
# ['Ernst','Blofeld'],
# ]
# with open('userlist1.csv','wt') as c_file:
#     csvout = csv.writer(c_file, delimiter=':')
#     csvout.writerows(namelist)
#     print(c_file)
#     
    
#     csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
# 使用DictWriter把字典类型的数据写入到csv文件中，如下
    
#     
# import csv
# villains = [
# {'first': 'Doctor', 'last': 'No'},
# {'first': 'Rosa', 'last': 'Klebb'},
# {'first': 'Mister', 'last': 'Big'},
# {'first': 'Auric', 'last': 'Goldfinger'},
# {'first': 'Ernst', 'last': 'Blofeld'},
# ]
# with open('userlist3.csv','at',newline='') as csvfile:
#     writer = csv.DictWriter(csvfile,['first','last'])
#     writer.writerows(villains)
#     
    
    
    
# JSON/pickle数据处理
    # python中使用json模块把复杂结构的数据转换成JSON字符串，或者把JSON字符串转换成数据。
menu =     {
    "breakfast": {
                "hours": "7-11",
                "items": {
                        "breakfast burritos": "$6.00",
                        "pancakes": "$4.00"
                        }
                },
    "lunch" : {
            "hours": "11-3",
            "items": {
                    "hamburger": "$5.00"
                    }
            },
    "dinner": {
            "hours": "3-10",
            "items": {
                    "spaghetti": "$8.00"
                    }
            }
    }    
    

# 1 转换成JSON字符串

# 使用dumps()将menu转换成JSON格式的字符串如下：
    
import json
menu_json = json.dumps(menu)    # str 字符串  json
print(menu_json)
    
# 2 转换成复杂结构的数据

# 使用loads()函数把JSON字符串转换成python的结构数据

menu2 = json.loads(menu_json)      # dict字典
print(menu2)

print(type(menu_json))
print(type(menu2))





    