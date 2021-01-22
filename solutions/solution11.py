n = int(input())
student_marks = {}

for marks in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

sum = 0

for mark in student_marks[query_name]:
    sum = sum + mark

print('{:.2f}'.format(sum/3))


