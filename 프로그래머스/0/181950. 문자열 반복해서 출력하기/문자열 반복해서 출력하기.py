str, n = input().strip().split(' ')

i = int(n)

if (len(str) >= 1 and len(str) <= 10) and (i >= 1 and i <= 5):
    print(str*i)
else: print("error")