A, B = input().split()

a = int(A[::-1])
b = int(B[::-1])

if a > b:
    print(a)
else:
    print(b)