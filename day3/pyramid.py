row=5
for i in range(1,row+1):
    print()
    for space in range(row-i):
        print(" " , end="")
    for star in range(2*i-1):
        print("*" , end="")

for i in range (1,row+2):
    print()
    for star in range(i):
        print("*", end="")

# for i in range (1,row+2):
#     print()
#     for star in range (row - i + 1 ):
#         print("*", end="")
