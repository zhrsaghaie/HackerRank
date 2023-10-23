#Lucid - trex-pushups


n =int(input())
terrain = list(map(int, input().split()))

p = 0
for i in range(n-1):
    if (terrain[i] - terrain[i+1] >= 4):
        p += 1

print(p)