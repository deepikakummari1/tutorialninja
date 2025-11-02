a=12345
while a>9:
    s=0
    for i in str(a):
        s=s+int(i)
    a=s
print(a)
