file = open('student.txt', 'r')

max_score = 0
min_score = 100
top_student = ''
bottum_student = ''
total_score = 0
count = 0

for line in file:
    name, score = line.split()
    score = int(score)

    total_score += score
    count += 1

    if max_score < score:
        max_score = score
        top_student = name

    if score < min_score:
        min_score = score
        bottum_student = name


file.close()

average = total_score / count

print("우등생은 %s입니다." % top_student)
print("열등생은 %s입니다." % bottum_student)
print("평균은 %.1f점입니다." % average)