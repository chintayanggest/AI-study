'''
💚 Challenge 1: Dictionary Basics
Create a dictionary called students where:
The keys are student names ("Alice", "Bob", "Maki")
The values are their ages (20, 22, 19)
Then:
Add a new student "John" with age 21.
Print out the age of "Maki".
Remove "Bob" from the dictionary.
Print the final dictionary.'''

my_dict = {
    "Alice" : 20,
    "Bob"   : 22,
    "Maki"  : 19
}

my_dict["Jhon"] = 21
print(f"The age of Maki is {my_dict['Maki']}")

my_dict.pop("Bob")

for name , age in my_dict.items():
    print(f"The age of {name} is {age}")



# ___________________________________________________________________________________________________________________#

'''
💚 Challenge 2 : Dictionaries can hold other dictionaries!
👉 Create a dictionary called classroom 
Print Maki’s grade.
Add a new student "Sara" with age 22 and grade "C".
Change Alice’s grade to "B".
Loop through and print each student’s name + grade.
'''

classroom = {
  "Alice": {"age": 20, "grade": "A"},
  "Maki": {"age": 19, "grade": "B"},
  "John": {"age": 21, "grade": "A"}
}
print(f"Maki's grade is {classroom['Maki']['grade']}")
classroom['Sara']={"age":22, "grade":"C"}
classroom["Alice"]['grade']="B"

for key , value in classroom.items():
    if isinstance (value,dict):
        for inner_key , inner_value in value.items():
            print(key,inner_key ,inner_value)