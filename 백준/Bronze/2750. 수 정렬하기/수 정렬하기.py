n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

lst.sort()
print(*lst,sep='\n')