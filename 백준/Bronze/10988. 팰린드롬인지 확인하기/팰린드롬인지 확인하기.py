s = input()
a = 0
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        a += 1
        print(0)
        break
if a == 0:
    print(1)