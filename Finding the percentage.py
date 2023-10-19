n = int(input('N = '))
student_marks = {}
for _ in range(n):
    name, *line = input('Name: ').split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input('Querry Name: ')
print(scores)