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

# ___________________________________________________________________________________________________________________#

x=20
for i in range (1,x+1):
      if i%3==0 and i%5==0:
            print("FizzBuzz")
      elif  i%3==0:
           print("Fizz")
      elif i%5==0:
            print("Buzz")
      else :
            print(i)

# ___________________________________________________________________________________________________________________#

x=[2,4,6,8,10]
for i in x:
     i=i*2
     print(i)

# ___________________________________________________________________________________________________________________#

# '''
# Create a function named square.
# It should take one number (as input).
# Inside, it should calculate the square of that number (number × number).
# Return the result.
# Outside the function, call it with the number 5, and print what it gives back.'''

def square(x):
    x*=x
    print(x)
square(5)
# '''👉 This will print 25, but result will be None, because the function didn’t return anything.'''

def square(x):
    return x*x
print(square(5))

'''⚡So:
Use print() when you just want to show something.
Use return when your function should produce a value that can be reused.'''

# ___________________________________________________________________________________________________________________#

x=("Python")
for i in x:
    print(i)

x=("Python")
for i in x[::-1]:
    print(i)

'''
string[start:stop:step]
start → where to start (default is 0)
stop → where to stop (default is the end)
step → how much to move each time
x[::-1]
start is empty → start at the beginning
stop is empty → go to the end
step = -1 → move backwards (negative step means reverse)'''

'''But later, if you forget, you can always use loops or the reversed() function — Python will give you multiple ways.'''

# ___________________________________________________________________________________________________________________#

x=int(input("Input a number : "))
while x!=0:
    print(f"You entered {x}")
    x=int(input("Input a number : "))
print("Goodbye!")

while True:
    x = int(input("Input a number: "))
    if x == 0:
        print("Goodbye!")
        break
    print(f"You entered {x}")