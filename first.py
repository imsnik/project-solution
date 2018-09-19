s = input()
j = list(s)
p = list(map(int, j))
lenp = len(p)
cost=[0,3.5,2.5,4,3.5,1.75,1.5,2.25,3.75,1.25]
final = 0
for i in range(0,lenp):
    final = final + cost[p[i]]
print('$',final)
