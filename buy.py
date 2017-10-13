n=input()
M1=input()

a=input().split( )

M2=input()

b=input().split( )
z
ab = list(set(b)-set(a))
ab.sort()
x=1
if(len(ab) == 0):
        print("None")
else:
    for i in ab:
        if(x!=len(ab)):
            print(i, end=' ')
        else:
            print(i)
        x+=1
