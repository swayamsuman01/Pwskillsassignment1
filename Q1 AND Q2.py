'''Q1 when to use For loop and while loop
   ans: when you know how many times you want to run the loop or how many times you want the output but when you want to run loop upto certain condition ,we use while loop'''

##Q2: sum and product of first 10 numbers using for loop
sum=0
for i in range(1,11) :
    
    sum=sum+i
print("sum of 10 numbers is",sum)

k=1
pro=1
while k<11 :
    
    pro=pro*k
    k=k+1
print("product is",pro)

