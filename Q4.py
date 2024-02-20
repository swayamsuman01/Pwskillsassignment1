lst=[i for i in range(1,101)]
lst2=[]
for i in lst :
    k=i*i*i
    if k%4==0 or k%5==0:
        lst2.append(i)
        print(lst2) 

