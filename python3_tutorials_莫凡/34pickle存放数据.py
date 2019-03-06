# pickle.dump(a_dict, file)
# a_dict1 = pickle.load(file)

import pickle

a_dict = {'da': 111, '2': [1, 3, 5]}

# file = open('pickle_example.pickle', 'wb')  # wb二进制

# pickle.dump(a_dict, file)

# file.close


# file = open('pickle_example.pickle', 'rb')
# a_dict1 = pickle.load(file)
# file.close()
# print(a_dict1)


# with简写,省去close()

with open('pickle_example.pickle', 'rb') as file:
    a_dict1 = pickle.load(file)
print(a_dict1)
