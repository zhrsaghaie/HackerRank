#Lucid - Museum Analytics

n =int(input())
dict ={}

for i in range(n):
    dina_list = input().split(',')
    for dina in dina_list:
        # dina = dina.replace("-", "").lower()
        if dina in dict:
            dict[dina] += 1
        else:
            dict[dina] = 1

# print(dict)
a = max(dict, key=dict.get)
print(a)
print(dict[a])


