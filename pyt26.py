x=int(input("Enter x:")) 
y=int(input("Enter y:")) 
z=int(input("Enter z:")) 
n=int(input("Enter n:"))

results=[]

for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if (i+j+k)!=n:
                results.append([i,j,k])
print(results)

