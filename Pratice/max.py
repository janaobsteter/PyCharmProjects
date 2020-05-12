# Enter your code here. Read input from STDIN. Print output to STDOUT
#use function product(*ListOfLists)
from itertools import product

k, m = map(int, input().split(" "))

lists = []
for l in range(0, k):
    lists.append([x for x in map(int, input().split(" "))])

if sum([m ^ 2 for m in [max(l) for l in lists]]) < m:
    print(sum([mx ** 2 for mx in [max(l) for l in lists]]))
else:
    print(max([(sum(map(lambda x: pow(x, 2), l)) % m, l) for l in product(*lists)]))