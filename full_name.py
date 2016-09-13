full_name = ("Donna","Shih", "Michelle", "Monica")

full_list = []
for name in full_name:
	full_list.append(name)
for i in range(len(full_list)-1,-1,-1):
	print full_list[i]

for i in range (1000,0,-100):
	print (i)

names = ["Steven", "Michael", "James"]
print names [0:2]
print names [1:]
print names [0] + " " + names [-1]
print names [1 ] + " " + names [2]
print names [-1 ] + " " + names [0]
print names [-1 ] + " " + names [1]
print names [1 ] + " " + names [0]
print names [0 ] + " " + names [1]
# print names (-1 ,-2)
# print names [1 , 0)
# print names [1 , 2]
	