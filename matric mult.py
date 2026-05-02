a=[[1,2],
[3,4]]
b=[[5,6],
[7,8]]
result=[[0,0],[0,0]]
for i in range(0,len(a)):
    for j in range(0,len(b)):
        for k in range(0,len(b)):
            result[i][j]+=a[i][k]*b[k][j]
print("Result Matrix")
for r in result:
    print(r)
