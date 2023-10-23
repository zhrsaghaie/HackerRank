n , g, p0, p1, p2= map(float, input().split())


for i in range(int(n)):    
    g = (1-g)* (1-g) * p0 + g * (1-g) * p1 * 2 + g * g * p2

print(float("{:.4f}".format(g)))
