char_list = ['a', 'b', 'b', 'c', 'c', 'c']

print(set(char_list))
print(type(set(char_list)))



sentence = 'Welcome Back to This Tutorial'

print(set(sentence))

unique_char = set(char_list)
unique_char.add('x') # add
print(unique_char)


# unique_char.clear()  # 清除

# unique_char.remove('x')  # 移除

# set交集
set1 = unique_char
set2 = {'a', 'b'}

print(set1.difference(set2))
print(set1.intersection(set2))# 交集





