# a=12345
# while a>9:
#     s=0
#     for i in str(a):
#         s=s+int(i)
#     a=s
# print(a)
# print()

l=[2,3,4,5,6]
a=10
for i in range(len(l)):
    for o in range(i+1,len(l)):
        sum=l[i]+l[o]
        if sum==a:
            print(l[i]+l[o])
            print(l[i],l[o])
