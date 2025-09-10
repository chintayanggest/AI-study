'''Can you try to write a small piece of Python code that:
Creates a dictionary of 3 countries and their capitals,
Adds one more country,
Prints all the capitals.'''

my_dict = {
    "Japan": "Tokyo", 
    "France": "Paris", 
    "Indonesia": "Jakarta"
    }

my_dict["USA"]="Washington-DC"
print(my_dict.values())

for country, capital in my_dict.items():
    print(f"The capital of {country} is {capital}")
