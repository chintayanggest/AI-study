# n = int(input("Enter a number : "))
# for i in range(1,n+1):
#     if i%3 == 0 :
#         continue
#     print(i)

# m = int(input("Enter a number : "))
# i=0
# while i < m :
#     i+=1
#     if i%3 == 0:
#         continue
#     print (i , end="")

# # ___________________________________________________________________________________________________________________#

# x=20
# for i in range (1,x+1):
#       if i%3==0 and i%5==0:
#             print("FizzBuzz")
#       elif  i%3==0:
#            print("Fizz")
#       elif i%5==0:
#             print("Buzz")
#       else :
#             print(i)

# # ___________________________________________________________________________________________________________________#

# x=[2,4,6,8,10]
# for i in x:
#      i=i*2
#      print(i)

# # ___________________________________________________________________________________________________________________#

# # '''
# # Create a function named square.
# # It should take one number (as input).
# # Inside, it should calculate the square of that number (number × number).
# # Return the result.
# # Outside the function, call it with the number 5, and print what it gives back.'''

# def square(x):
#     x*=x
#     print(x)
# square(5)
# # '''👉 This will print 25, but result will be None, because the function didn’t return anything.'''

# def square(x):
#     return x*x
# print(square(5))

# '''⚡So:
# Use print() when you just want to show something.
# Use return when your function should produce a value that can be reused.'''

# # ___________________________________________________________________________________________________________________#

# x=("Python")
# for i in x:
#     print(i)

# x=("Python")
# for i in x[::-1]:
#     print(i)

# '''
# string[start:stop:step]
# start → where to start (default is 0)
# stop → where to stop (default is the end)
# step → how much to move each time
# x[::-1]
# start is empty → start at the beginning
# stop is empty → go to the end
# step = -1 → move backwards (negative step means reverse)'''

# '''But later, if you forget, you can always use loops or the reversed() function — Python will give you multiple ways.'''

# # ___________________________________________________________________________________________________________________#

# x=int(input("Input a number : "))
# while x!=0:
#     print(f"You entered {x}")
#     x=int(input("Input a number : "))
# print("Goodbye!")

# while True:
#     x = int(input("Input a number: "))
#     if x == 0:
#         print("Goodbye!")
#         break
#     print(f"You entered {x}")

# # ___________________________________________________________________________________________________________________#

# '''Make a program that:
# Has a list of numbers: [3, 7, 12, 18, 25, 30]
# Loops through the list.
# For each number:
# If it’s even, print: "X is even"
# If it’s odd, print: "X is odd"'''

# x=[3,7,12,18,25,30]
# for i in x:
#     if i%2==0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# # ___________________________________________________________________________________________________________________#

# # '''Make a program that:
# # Asks the user to enter 5 numbers (one by one).
# # Stores them in a list.
# # After all numbers are entered, print the list.'''
# # '''From the list you just created, print:
# # The maximum number
# # The minimum number
# # The sum of all numbers'''

# x=[]
# count=0
# while count <5:
#     y = int(input("Input a number:"))
#     x.append(y)
#     count +=1
# print(x)

# # first way 
# # print(f"the max of the list is {max(x)}")
# # print(f"the min of the list is {min(x)}")

# sum=0
# for i in x:
#     sum+=i
# print(f"the sum is {sum}")

# #second way
# # x.sort()
# # print(f"the min is {x[0]}")
# # print(f"the max is {x[4]}")

# #third way
# #use loop
# min=x[0] #this is initialize min = the first on "x" list the first number
# max=0
# for i in x:
#     if i<min:
#         min=i
#     elif i>max:
#         max=i
# print(f"the min number is {min}")
# print(f"the max number is {max}")

#  # ___________________________________________________________________________________________________________________#

# '''The better version of the above code 
# most of the code use loop to find the result and do not use min and max as variabel cause it can overwrite built in python'''

# x = []
# count = 0

# while count < 5:
#     y = int(input("Input a number: "))
#     x.append(y)
#     count += 1

# print(x)

# # Sum using loop
# total = 0
# for i in x:
#     total += i
# print(f"The sum is {total}")

# # Find min and max using loop
# min_num = x[0]  # initialize with the first element
# max_num = x[0]

# for i in x:
#     if i < min_num:
#         min_num = i
#     elif i > max_num:
#         max_num = i

# print(f"The min number is {min_num}")
# print(f"The max number is {max_num}")

#  # ___________________________________________________________________________________________________________________#

# '''
# Asks the user to input 5 numbers (store them in a list).
# Counts how many numbers are even and how many are odd.
# Prints the counts at the end.'''

# x=[]
# odd_num_count = 0
# even_num_count = 0
# count = 0
# while count < 5 :
#     y = int(input(f"Input a number :"))
#     count +=1
#     x.append(y) 
# print(x)
# for i in x:
#     if i%2 == 0:
#         even_num_count +=1 
#     else :
#         odd_num_count +=1
# print(f"Total even number is {even_num_count}")
# print(f"Total odd number is {odd_num_count}")


# '''used a for loop instead of while for cleaner iteration.
# Variable names slightly simplified (even_count instead of even_num_count).
# Printed the numbers list in a neat way.'''
# numbers = []  
# even_count = 0  
# odd_count = 0  

# for i in range(5):  
#     num = int(input("Input a number: "))  
#     numbers.append(num)  

# for num in numbers:  
#     if num % 2 == 0:  
#         even_count += 1  
#     else:  
#         odd_count += 1  

# print(f"Numbers: {numbers}")  
# print(f"Total even numbers: {even_count}")  
# print(f"Total odd numbers: {odd_count}")  



 # ___________________________________________________________________________________________________________________#

'''👉 Write a program that asks the user to input a list of numbers (keep taking inputs until the user enters 0).
Then:
Print the list of numbers entered.
Find and print the sum of all positive numbers.
Find and print the sum of all negative numbers.'''

numbers = int(input("Input a number : "))
listOfNum = []
sumOfPositiveNum = 0
sumOfNegativeNum = 0

while numbers != 0:
    numbers = int(input("Input a number : "))
    listOfNum.append(numbers)
    if numbers > 0:
        sumOfPositiveNum += numbers
    else :
        sumOfNegativeNum += numbers

print(listOfNum)        
print(f"The sum of Positive numbers is : {sumOfPositiveNum}")
print(f"The sum of Negative numbers is : {sumOfNegativeNum}")