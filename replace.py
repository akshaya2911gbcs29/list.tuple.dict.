n=input("Enter a sentence:").split()
d={}
d["store"]="shop"
d["car"]="bike"
for i in n:
   if i in d:
      i=d[i]
      print(i,end=" ")
   else:
      print(i,end=" ")
