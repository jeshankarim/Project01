cakeangle=int(input("Enter the Angle of the Cake: "))
N=int(input("Enter the no of pieces of the Cake: "))
if(cakeangle%N==0):
    print("YES the cake will cut in equal pieces of size %d"%N)
else:
    print("NO the cake will not cut in equal pieces of size %d"%N)
if(N>cakeangle):#only when N is greater the cake angle cake can't be cut into pieces
    print("NO the cake will not cut in any pieces of size %d"%N)
else:
    print("YES the cake will cut in any pieces of size %d"%N)
n=1 #start substracting the cake 
for i in range(N):
    n+=1
    cakeangle=N
    if (cakeangle<0):
        print("NO the cake will not cut into %d pieces such that no two of them are equal"%N)
        break
    else:
        print("YES the cake will cut into %d pieces such that no two of them are equal"%N)