#Lucid - Watering Holes

n = int(input())

dic_dina = {}
dic_hole = {}



for i in range(n):
    park_log = input().split()
    hole = int(park_log[1])
    dina = park_log[0]
    dic_dina[dina] = hole
    dic_hole[hole] = []

for dina, hole in dic_dina.items():
    if hole != 0:
        if hole in dic_hole:
            dic_hole[hole].append(dina)
        else:
            dic_hole[hole] = [dina]

dic_hole = dict(sorted(dic_hole.items()))
# print("-----------\n")
# print(dic_hole)
# print("-----------\n")
for hole, dinas in dic_hole.items():
    if hole != 0:
        dic_hole[hole] = sorted(dic_hole[hole])
        if len(dic_hole[hole]) > 0 :
            print (hole ,*dic_hole[hole])
        else:
            print(hole , "n/a")


