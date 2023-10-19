n = int(input('N = '))

record = []

for i in range(n):
    name = input('Name: ')
    score = float(input('Score: '))
    record.append([name, score])
print(record)

second_highest = sorted(list(set([marks for name, marks in record])))[1]
print('\n'.join([a for a,b in sorted(record) if b == second_highest]))