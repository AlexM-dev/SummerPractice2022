a = input().split(';')
n = ''

for i in range(len(a)):
    if a[i].isdigit():
        a[i] = int(a[i])

for i in range(len(a)):
    if type(a[i]) == int:
        if a[i] % 2 == 0:
            n+=f'{a[i]},'

for i in range(len(a)):
    if type(a[i]) == int:
        if a[i] % 3 == 0:
            n+=f'{a[i]},'

for i in range(len(a)):
    if type(a[i]) == str:
        if len(a[i]) > 4:
            n+=f'{a[i]},'

if len(n) > 0:
    if n[-1] == ",":
        n = n[:-1]

print(n)