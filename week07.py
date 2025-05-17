# # 7주차

# 1. 사용자로부터 이름을 입력받아, `name.txt` 파일에 저장하시오.

# ```python
# (입력) Alice
# (파일 내용) Alice
# ```

# ```python
name = input()
with open("name.txt", "w") as f:
    f.write(name)
# ```


# **2번 문제부터의 조건:** 파일은 미리 존재하며, 여러 줄이 있을 수 있음.

# 2. `hello.txt` 파일에서 첫 번째 줄만 읽어서 출력하시오.

# ```bash
# (파일 내용)
# Hello
# World

# (출력) Hello
# ```

# ```python
with open("hello.txt", "r") as f:
    line = f.readline()
print(line.strip())
# ```


# 3. `data.txt` 파일에 있는 모든 텍스트에서 단어의 개수를 세어 출력하시오.

# ```python
# (파일 내용)
# Python is fun.

# (출력) 3
# ```

# ```python
with open("data.txt", "r") as f:
    text = f.read()
    
words = text.split()
print(len(words))
# ```


# 4. `log.txt` 파일에서 "error"라는 단어가 포함된 줄만 모두 출력하시오.

# ```bash
# (파일 내용)
# ok
# error: file not found
# success
# error: invalid input

# (출력)
# error: file not found
# error: invalid input
# ```

# ```python
with open("log.txt", "r") as f:
    for line in f:
        if "error" in line:
            print(line.strip())
# ```


# 5. `words.txt` 파일에서 단어별 등장 횟수를 세어 딕셔너리 형태로 출력하시오. 모든 단어는 소문자로 가정.

# ```python
# (파일 내용)  
# apple banana apple orange banana apple

# (출력) {'apple': 3, 'banana': 2, 'orange': 1}
# ```

# ```python
with open("words.txt", "r") as f:
    text = f.read()
    
words = text.split()

counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1
        
print(counts)
# ```


# 6. `num.txt` 파일에 공백으로 구분된 숫자들이 저장되어 있다. 이 숫자들 중 **짝수만 골라서** `even.txt` 파일에 **한 줄에 하나씩** 저장하시오.

# ```bash
# (파일 내용: num.txt)  
# 1 2 3 4 5

# (생성될 파일 내용: even.txt)  
# 2  
# 4

# ```

# ```python
with open("num.txt", "r") as f:
    nums = list(map(int, f.read().split()))

with open("even.txt", "w") as f:
    for n in nums:
        if n % 2 == 0:
            f.write("%d\n" % n)
# ```


# 7. `student.txt` 파일에는 각 학생의 이름과 점수가 한 줄에 하나씩 저장되어 있다.
# 이 파일을 읽어서 **가장 높은 점수를 받은 학생**과 **전체 평균 점수**를 구하시오.

# 다음은 `student.txt` 파일

# ```python
# Alice 70  
# Bob 60  
# Cat 90  
# Dil 50  
# Dobby 80
# ```

# 다음은 출력 결과

# ```python
# 우등생은 Cat입니다.
# 평균은 70.0점입니다.
# ```

# ```python
file = open('student.txt', 'r')

max_score = 0
top_student = ''
total_score = 0
count = 0

for line in file:
    name, score = line.split()
    score = int(score)

    total_score += score
    count += 1

    if score > max_score:
        max_score = score
        top_student = name

file.close()

average = total_score / count

print("우등생은 %s입니다." % top_student)
print("평균은 %.1f점입니다." % average)
# ```