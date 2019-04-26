aaa={}
def add(key,value):
    aaa.setdefault(key,[])
    aaa[key].append(value)

add(12,1102)
# print (aaa)

add(13,1113)
# print (aaa)

#
# print (aaa)

add(13,11056)
# print (aaa[12])

list=aaa.pop(12)
print(list)

for i in list:
    print(i)
