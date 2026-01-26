'''Ahmedfarooqui'''
'''UIN:- 251P090'''
print("Ahmed Farooqui")
print("UIN:-251P090")
rows = int(input("Enter number of rows:"))

'''for i in range(1,rows+1):
    for j in range(i):
        print("*",end="")
    print()'''

'''i=1
while(i<=rows):
    j=1
    while(j<=i):
        print("*",end="")
        j+=1
    print()
    i+=1'''
i=1
while True:
    j=1
    while True:
        print("*",end="")
        j+=1
        if j>i:
            break
    print()
    i+=1
    if i> rows:
        break