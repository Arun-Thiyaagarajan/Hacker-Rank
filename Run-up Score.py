n = int(input('N = '))
arr = map(int, input(f'Enter {n} Elements: ').split())

a = list(arr)
m1 = max(a)
m2 = [i for i in a if i != m1]
print(max(m2))