
'''
Write a program that:
Asks the user for a sentence (string).
Counts how many vowels (a, e, i, o, u) are in it.
Ignores uppercase vs lowercase.
Prints:
The original sentence.
The total vowel count.
Which vowel appears the most, and how many times.
⚔️ Extra Challenge (bonus XP):
Also display the vowels sorted from most frequent to least frequent.'''

x = input("Enter a sentence : ")
my_dict = {"a" : 0 , "i" : 0 , "u" : 0 , "e" : 0 , "o" : 0}
count = 0

for y in x.lower():
    # if y == "a":
    #     my_dict["a"] += 1
    #     count += 1
    # elif y == "i":
    #     my_dict["i"] += 1
    #     count += 1
    # elif y == "u":
    #     my_dict["u"] += 1
    #     count += 1
    # elif y == "e":
    #     my_dict["e"] += 1
    #     count += 1
    # elif y == "o":
    #     my_dict["o"] += 1
    #     count += 1
    '''this one better (eventhough the result is same)'''
    if y in my_dict:
        my_dict[y] += 1
        count += 1

'''
Way to sorting a dictionary
# Sample dictionary
my_dict = {'apple': 3, 'banana': 1, 'orange': 2, 'grape': 4}

# Sort by value in ascending order
sorted_items_asc = sorted(my_dict.items(), key=lambda item: item[1])
# Convert the sorted list of tuples back to a dictionary (Python 3.7+ maintains insertion order)
sorted_dict_asc = dict(sorted_items_asc)'''

sorted_items_dsc = sorted(my_dict.items() , key=lambda item : item[1] ,reverse=True)
# sorted_dict_dsc = dict(sorted_items_dsc) this line will convert the sorted tupple back to dick , just do it if its necessary 

# highest_value = max(my_dict.values()) this will only print value of max item
# highest_key = max(my_dict , key = my_dict.get) this only key of max item

highest_key , highest_value = max(my_dict.items(), key= lambda item : item[1])

print(f"The sentence : '{x}'")
print(f"The total vowel count : {count}")
print(f"The most frequent vowel is : '{highest_key}' appears {highest_value} times")
print(f"The vowels from most frequent to least frequent {sorted_items_dsc}")




 # ___________________________________________________________________________________________________________________#