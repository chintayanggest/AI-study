n = int(input("Enter a number : "))
for i in range(1,n+1):
    if i%3 == 0 :
        continue
    print(i)

m = int(input("Enter a number : "))
i=0
while i < m :
    i+=1
    if i%3 == 0:
        continue
    print (i , end="")