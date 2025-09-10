# '''
# Asks the user to enter 5 numbers and stores them in a list.
# Creates three separate functions:
# get_max(numbers) → returns the maximum number in the list
# get_min(numbers) → returns the minimum number in the list
# get_sum(numbers) → returns the sum of all numbers in the list'''

# numbers = []

# for i in range(5):
#     num = int(input("Input a number : "))
#     numbers.append(num)
# print(numbers)

# def get_max(x):
#     max_num = x[0]
#     for i in x:
#         if i > max_num:
#             max_num = i
#     return max_num

# def get_min(y):
#     min_num = y[0]
#     for i in y:
#         if i < min_num:
#             min_num = i
#     return min_num

# def get_sum(z):
#     sum_num = 0
#     for i in z:
#         sum_num += i 
#     return sum_num

# print(f"Max number is : {get_max(numbers)}")
# print(f"Min number is : {get_min(numbers)}")
# print(f"The sum is : {get_sum(numbers)}")



# # ___________________________________________________________________________________________________________________#

# '''
# Write a program that:
# Asks the user to enter 5 numbers and stores them in a list.
# Creates a function classify_numbers(numbers) that:
# Loops through the list.
# Prints "X is even" if the number is even.
# Prints "X is odd" if the number is odd.
# Calls classify_numbers(numbers) after the input and prints the results'''

# numbers = []

# for i in range(5):
#     num = int(input("Input a number : "))
#     numbers.append(num)
# print(numbers)

# def classify_numbers(numbers):
#     for i in numbers:
#         if i%2==0:
#             print(f"{i} is even")
#         else :
#             print(f"{i} is odd ")

# classify_numbers(numbers)



#  # ___________________________________________________________________________________________________________________#

# '''
# Write a program that:
# Uses a while loop to let the user input numbers one by one.
# Stop when the user types 0.
# Stores all numbers (except 0) in a list.
# Creates a function analyze_numbers(numbers) that:
# Prints the sum of all numbers.
# Prints the maximum number.
# Prints the minimum number.
# Calls analyze_numbers(numbers) after the input is done'''

# numbers = []

# num = int(input("Input a number : "))
# while num != 0:
#     numbers.append(num)
#     num = int(input("Input a number : "))
# print(numbers)

# def analyze_numbers(numbers):
#     num_sum = 0
#     max_num = numbers[0]
#     min_num = numbers[0]

#     for i in numbers:
#         num_sum += i
#         if i > max_num:
#             max_num=i
#         elif i < min_num:
#             min_num = i
        
#     print(num_sum)
#     print(max_num)
#     print(min_num)

# analyze_numbers(numbers)



#  # ___________________________________________________________________________________________________________________#

# '''
# Write a program that:
# Lets the user input numbers until they type 0 (store them in a list).
# Creates a function classify_numbers(numbers) that:
# Loops through the list.
# Prints "X is positive" if the number is greater than 0.
# Prints "X is negative" if the number is less than 0.
# Prints "X is even" if the number is even.
# Prints "X is odd" if the number is odd.
# Each number may get multiple classifications (e.g., -4 → “negative” and “even”).
# Calls classify_numbers(numbers) after input is done.'''

# numbers = []

# num = int(input("Input a number : "))
# while num != 0:
#     numbers.append(num)
#     num = int(input("Input a number : "))
# print(numbers)    

# def classify_numbers(numbers):
#     for i in numbers:
#         if i > 0 and i % 2 == 0 :
#             print(f"{i} is a positive and even number")
#         elif i > 0 and i % 2 != 0 :
#             print(f"{i} is a positive and odd number")
#         elif i < 0 and i % 2 == 0 :
#             print(f"{i} is a negatif and even number") 
#         elif i < 0 and i % 2 != 0 :
#             print(f"{i} is a negatif and odd number")

# classify_numbers(numbers)



#  # ___________________________________________________________________________________________________________________#

# '''Write a Python function called greet that takes a single argument, name (a string), and prints a personalized greeting to the console.'''

# def greet (x):
#     print(f"Hello, {x}")

# greet("Alice")


# # ___________________________________________________________________________________________________________________#
# '''Write a Python function called sum_even_numbers that takes a list of integers as an argument and returns the sum of all the even numbers in that list.'''


# def sum_even_numbers(numbers):
#     count = 0
#     for i in numbers:
#         if i % 2 == 0:
#             count +=i
#     return count       

# numbers = [1,2,3,4,5,6,7,8,9,10]
# total = sum_even_numbers(numbers)
# print(f"The sum is {total}")

# #a more compact "Pythonic" way to write this uses a list comprehension:
# def sum_even_numbers_pythonic(numbers):
#     return sum([num for num in numbers if num % 2 == 0])

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(f"The sum is {sum_even_numbers_pythonic(numbers)}")

# def invert_dictionary(my_dict):


#  # ___________________________________________________________________________________________________________________#

'''
Write a program that:
Asks the user to enter a sentence.
Implements a function analyze_sentence(sentence) that returns a dictionary with this structure:
{
  "total_vowels": int,                # total vowel count in the whole sentence
  "vowel_counts": {"a":int, ...},     # counts for each vowel (a,e,i,o,u)
  "most_frequent_vowels": [ ... ],    # list of vowel(s) with highest count (handle ties)
  "sorted_vowels": [("a",count), ...],# vowels sorted from most → least frequent
  "per_word": [                        # list, one dict per word
      {"word": "hello", "total": 2, "vowels": {"a":0,...}},
      ...
  ]
}
Counting rules:
Ignore case (treat A same as a).
Count only alphabetic characters for vowels (ignore digits/punctuation).
Split words by whitespace for the per_word list.
The main program should call analyze_sentence, then print the returned results in a readable format (you decide layout).
Rules:
Use dictionaries and lists (no collections.Counter).
The function must return the dictionary (don’t just print inside the function).
Handle ties for most frequent vowels by returning all tied vowels in the most_frequent_vowels list.
'''
my_dict = {"total_vowels" : 0 ,
           "vowel_count" : {"a" : 0 , "i" : 0 , "u" : 0 , "e" : 0 , "o" : 0},
           "most_frequent_vowels" : [],
           "sorted_vowels" : [("a", 0),("i" , 0),("u" ,0) ,("e",0), ("o" , 0)],
           "per_word" : 
                [{"word": "", "total" : 0 , "vowels" : {"a" :0, "i" : 0 , "u" : 0 , "e" :0 , "o" : 0}},
                {"word": "", "total" : 0 , "vowels" : {"a" :0, "i" : 0 , "u" : 0 , "e" :0 , "o" : 0}}]
           }
