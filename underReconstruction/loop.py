# import json

# def main():

#     # create a simple JSON array
#     jsonString = '{"key1":"value1","key2":"value2","key3":"value3"}'

#     # change the JSON string into a JSON object
#     jsonObject = json.loads(jsonString)

#     # print the keys and values
#     for key in jsonObject:
#         value = jsonObject[key]
#         print("The key and value are ({}) = ({})".format(key, value))

#     pass

# if __name__ == '__main__':
#     main()

# # for restaurant in data['restaurants']:
# #     print restaurant['restaurant']['name']

listp = {1:'f', 2: 'g', 3: 'p'}
print(type(listp))


a = listp.items()
print(a)
for item in listp:
    if listp.keys() == 2