# import json                # ПОДКЛЮЧЕНИЕ ФАЙЛА Json to Python

# json_file_path = "Projects\data_file.json"

# # Working
# with open(json_file_path, 'r') as j:
#      contents = json.loads(j.read())

# # print(contents)
# #_____

# # + Working
# # user = input("User: ")
# with open(json_file_path, 'r') as j:
#     contents = json.loads(j.read())

# # #print(contents)  

# code =  contents["users"][user]["pass"]
# display = contents["users"][user]["display"]

# print("Password: " + code)
# print("Display Name - " + display)
#+++++++++++++++++++++++++++++
import json                # ПОДКЛЮЧЕНИЕ ФАЙЛА Json to Python

json_file_path = "Projects\data_file.json"

user_in = input("User: ")

with open(json_file_path, 'r') as j:
    contents = json.loads(j.read())
    if contents["Richard"]["display"] == user_in:
        print('Hi!')

# code =  contents["users"][user]["pass"]
# display = contents["users"][user]["display"]

# print("Password: " + code)
# print("Display Name - " + display)

# {
#     "users":{
#       "User1": {
#         "display": "User1",
#         "pass": "EzPass123"
#       },
#       "Richard": {
#         "display": "Attack69",
#         "pass": "Smith"
#       }
#     }
#   }