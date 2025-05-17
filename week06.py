# # 2차 시험 대비

# 1. 정수를 입력받아 짝수인지 홀수인지 판별하여 출력하시오.

# ```python
# (입력) 3
# (출력) 3은 홀수이고 prime입니다.
# ```

# ```java
# (입력) 10
# (출력) 10은 짝수이고 prime이 아닙니다.
# ```

# ```python
# (입력) 0
# (출력) 0은 zero이고 prime이 아닙니다.
# ```

# ```python
n = int(input())

if n == 0:
    pos_str = "zero이고"
    is_prime = False
else: 
    if n % 2 == 1:
        pos_str = " 홀수이고"
    elif n % 2 == 0:
        pos_str = " 짝수이고"

    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break

if is_prime == True:
    prime_str = "prime입니다."
else: prime_str = "prime이 아닙니다."

print("%d은 %s %s" % (n, pos_str, prime_str))
# ```


# 2. 1부터 100까지의 수 중 짝수만 더한 합을 구하시오.

# ```python
# (출력) 1부터 100까지의 짝수 합은 2550입니다.
# ```

# ```python
even_sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i

print("1부터 100까지의 짝수 합은 ", even_sum, "입니다.", sep='')
# ```


# 3. 학생들의 이름과 성적을 입력받아, "최고 점수 학생은 [이름]이며, 평균 점수는 [평균 점수]입니다."를 출력하는 프로그램을 작성하시오. (소수점 첫째 자리까지 출력)

# ```python
# 몇 명에 대한 입력을 받겠습니까? (입력) 5
# 학생 1 이름: (입력) Alice
# 학생 1 성적: (입력) 85
# 학생 2 이름: (입력) Bob
# 학생 2 성적: (입력) 92
# 학생 3 이름: (입력) Cat
# 학생 3 성적: (입력) 91
# 학생 4 이름: (입력) Dil
# 학생 4 성적: (입력) 78
# 학생 5 이름: (입력) Dobby
# 학생 5 성적: (입력) 88

# (출력) 최고 점수 학생은 Bob이며, 평균 점수는 86.8입니다.
# ```

# ```python
students = int(input("몇 명에 대한 입력을 받겠습니까? "))

names = []
scores = []

# 학생 이름과 성적 입력받기
for i in range(students):
    name = input("학생 %d 이름: " % (i + 1))
    score = int(input("학생 %d 성적: " % (i + 1)))
    names.append(name)
    scores.append(score)

# 최고 점수 학생 찾기
max_score = max(scores)
max_index = scores.index(max_score)
top_student = names[max_index]

# 평균 점수 구하기
average_score = sum(scores) / len(scores)

# 출력
print("최고 점수 학생은 ", top_student, "이며, 평균 점수는 ", round(average_score, 1), "입니다.", sep='')
# ```

# 4. 문자열을 입력받아 각 문자가 몇 번 나왔는지 딕셔너리로 출력하시오.

# ```python
# (입력) hi i live in hawai
# (출력) 가장 많은 철자는 i이고, 5번 나왔어요.
# ```

# ```python
text = input().replace(" ", "")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

max_char = max(char_count, key=char_count.get)
# 또는 아래 주석된 방법으로
# max_char = ''
# max_count = 0

# for char, count in char_count.items():
#     if count > max_count:
#         max_char = char
#         max_count = count
max_count = char_count[max_char]

print("가장 많은 철자는 ", max_char, "이고, ", max_count, "번 나왔어요.", sep='')
# ```


# 5. 과목 이름과 점수를 공백으로 입력받아 딕셔너리를 만들고, 평균 점수보다 높은 과목의 이름을 리스트로 출력하시오.

# ```python
# (입력) math 80 english 90 science 70
# (출력) 입력된 과목의 수는 3이고, 평균은 80입니다.
# 평균 이상의 과목은 math, english입니다.
# 평균 이상의 과목의 평균은 85입니다.
# ```

# ```python
data = input().split()  # 입력 받아 공백 기준으로 나눔

scores = {}

# 과목과 점수 딕셔너리에 저장
for i in range(0, len(data), 2):
    subject = data[i]
    score = int(data[i + 1])
    scores[subject] = score

# 전체 평균 계산
total_avg = sum(scores.values()) // len(scores)

# 평균 이상 과목 찾기
above_avg_subjects = []
above_avg_scores = []

for subject, score in scores.items():
    if score >= total_avg:
        above_avg_subjects.append(subject)
        above_avg_scores.append(score)

# 평균 이상 과목의 평균
above_avg = sum(above_avg_scores) // len(above_avg_scores)

print("입력된 과목의 수는 %d이고, 평균은 %d입니다." % (len(scores), total_avg))
print("평균 이상의 과목은 %s입니다." % ', '.join(above_avg_subjects))
print("평균 이상의 과목의 평균은 %d입니다." % above_avg)
# ```


# 6. 정수들을 입력받아 중복 없이 정렬된 리스트를 출력하시오.

# ```python
# (입력) 3 1 2 3 2 1
# (출력) [1, 2, 3]
# ```

# ```python
lst = list(map(int, input().split()))

unique_sorted = []
for num in lst:
    if num not in unique_sorted:
        unique_sorted.append(num)

unique_sorted.sort()

print(unique_sorted)
# ```


# 7. 정수 리스트와 정수를 입력받아, 해당 값이 리스트의 몇 번째에 있는지 출력하시오. 값이 없으면 "없음"을 출력하시오.

# ```python
# (입력) 1 2 5 7 8 0
# (입력) 5
# (출력) 3
# ```

# ```python
nums = list(map(int, input().split()))
target = int(input())

if target in nums:
    print(nums.index(target) + 1)
else:
    print("없음")
# ```


# 8. 여러 개의 이름-나이 쌍을 입력받고, 특정 이름이 있는지 확인하시오.

# ```python
# (입력) Alice 20 Bob 25 Dobby 7
# (입력) Dobby
# (출력) Dobby는 7살입니다.
# ```

# ```python
person = input().split()

d = {}
for i in range(0, len(person), 2):
    name = person[i]
    age = int(person[i+1])
    d[name] = age

check = input()
if check in d:
    print(check, "는 ", d[check], "살입니다.", sep='')
else:
    print("없음")
# ```