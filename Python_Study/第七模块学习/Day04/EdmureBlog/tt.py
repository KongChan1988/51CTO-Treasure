__author__ = 'Administrator'

dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# print(dic.keys())
# for k,v in dic.items():
#     if k == 'k2':
#         del dic[k]

for k in list(dic.keys()):
    if k == 'k2':
        del dic[k]
print(dic)