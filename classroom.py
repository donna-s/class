# class_room=['chair', 'projector']
# new_items='snacks', 'comp'
# (1) class_room.append(new_items)
# (2) class_room=['snacks', 'comp']+class_room
# (3) class_room.extend(new_items)

# (4) class_room.insert(1,'markers')
# (1) del class_room[1]
# (2) del class_room[-3]
# (3) class_room.pop(1)
# print class_room

# for item in [1,3,5,7,9,11]:
# for item in range(17):
# for item in range(17,33):
# for item in range(17,33,2):
#   print item,

# for item in range (1,21):
#     if item == 13:
#         print "hello"
#     else:
#         print item,

# fruits = ['apples', 'oranges', 'bananas']
# places=0
# while places < len(fruits):
#     print fruits[places],
#     places+=1

# lengthlist = len(fruits)

# for item in range(lengthlist):
#     print fruits[item],


# def sum_nums(num):
#     calc =0
#     for item in range(0,num):
#         # calc = item + calc  
#         # calc = calc + item
#         calc += item
#     return calc  
# print sum_nums(4)
def sum_num2(num):
    calc =0
    for item in range(num,0):
        calc += item
    return calc  
print sum_num2(-3)

# count = 0
# while count <=20:
#     if count == 13:
#         print "hello"
#     else:
#         print count,
#     count+=1

# count = 0
# while count <=100:
#     print count
#     count+=10