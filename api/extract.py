import json
import pandas as pd

Url_path = "JsonFile\data .json"
with open(Url_path, 'r') as j:
     contents = json.loads(j.read())
mylist = []
for name in contents:
    mylist.append(name)
newdata = mylist['ocrInfomation']
print(newdata)



# def flatten_json(nested_json):
#     out = {}

#     def flatten(x, name=''):
#         if type(x) is dict:
#             for a in x:
#                 flatten(x[a], name + a + '_')
#         elif type(x) is list:
#             i = 0
#             for a in x:
#                 flatten(a, name + str(i) + '_')
#                 i += 1
#         else:
#             out[name[:-1]] = x

#     flatten(nested_json)
#     return out

# print(flatten_json(contents))