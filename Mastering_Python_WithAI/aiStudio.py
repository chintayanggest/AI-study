'''1️⃣Write a Python script that loops through model_config and prints out all the configuration details. The output should look exactly like this (the indentation is important):'''
# Config: model_name, Value: SimpleNet
# Config: version, Value: 1.2
# --- Parameters ---
#     Param: learning_rate, Value: 0.01
#     Param: epochs, Value: 50
#     --- Optimizer Params ---
#         Opt Param: beta1, Value: 0.9
#         Opt Param: beta2, Value: 0.999
# Config: active, Value: True

model_config = {
    "model_name": "SimpleNet",
    "version": 1.2,
    "parameters": {
        "learning_rate": 0.01,
        "epochs": 50,
        "optimizer_params": {
            "beta1": 0.9,
            "beta2": 0.999
        },
    "anton":12
    },
    "active": True
}

for key , value in model_config.items():
    if isinstance(value, dict): 
        print("--- Parameters ---")
        for inner_key, inner_value in value.items():
            if isinstance(inner_value, dict):
                print("\t--- Obtimizer Params ---")
                for innner_key, innner_value in inner_value.items():
                    print(f"\t\tOpt Param: {innner_key}, Value: {innner_value}")
            else:
                print(f"\tParam: {inner_key}, Value: {inner_value}")
    else:
        print(f"Config:{key}, Value: {value}")



#‼️‼️Important‼️‼️
'''Understand execution flow !
if we use the code below its wrong even if the output the same as above
because if im not move the the second if
the output gonna be wrong if there is more condition that meet the first if condition statement because
the looping happen first after its finsih then the second if happen
so if there is condition that meet the first if condition statement it gonna be the one the second if apply to
so the value is the last value that loop hold thats where the second if apply to
that makes the wrong output cause its not reach the other list in that dictionary'''
# for key , value in model_config.items():
#     if isinstance(value, dict): 
#         print("--- Parameters ---")
#         for inner_key, inner_value in value.items():
#             print(f"\tParam: {inner_key}, Value: {inner_value}")
#         if isinstance(inner_value, dict):
#             print("\t--- Obtimizer Params ---")
#             for innner_key, innner_value in inner_value.items():
#                 print(f"\t\tOpt Param: {innner_key}, Value: {innner_value}")
#     else:
#         print(f"Config:{key}, Value: {value}")



# ___________________________________________________________________________________________________________________#


'''2️⃣Your mission is to write a Python script that iterates through this users_data list, finds the email address for each user (no matter where it's hidden), and adds it to a new list.
The Desired Final Output:
After your code runs, you should have a new list that looks like this:
['alice@example.com', 'bob_b@workplace.net', 'char.lie@email.org']

'''
users_data = [
    {
        "id": 101,
        "name": "Alice",
        "email": "alice@example.com"
    },
    {
        "id": 102,
        "name": "Bob",
        "contact_details": {
            "email": "bob_b@workplace.net",
            "phone": "555-9876"
        }
    },
    {
        "id": 103,
        "name": "Charlie",
        "email": "char.lie@email.org"
    }
]

emails=[]

for i in users_data:
    for key , value in i.items():
        if isinstance (value,dict):
            for inner_key , inner_value in value.items():
                if inner_key == "email":
                    emails.append(inner_value)
        elif key == "email":
            emails.append(value)
print(emails)