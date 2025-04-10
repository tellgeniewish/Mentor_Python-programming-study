# (입력)과 (출력) 다음에 띄워쓰기 하나는 보기 편하라고 그렇게 적은거니까 무시하기!

# # 리스트

# 1. 리스트 `[1, 2, 3, 4, 5]`에서 마지막 원소를 출력하시오.
num = [1, 2, 3, 4, 5]
print(num[-1])
#     ```python
#     (입력) 없음
#     (출력) 5
#     ```
    

# 2. 리스트 `[3, 6, 9]`에 원소 12를 추가하고 출력하시오.
arr = [3, 6, 9]
arr.append(12)
print(arr)
#     ```python
#     (입력) 없음
#     (출력) [3, 6, 9, 12]
#     ```
    

# 3. 정수를 입력받아 리스트에 저장한 후, 합계를 출력하시오.
c = int(input("몇 번 입력받을래? "))
nums = []
for i in range(c):
    nums.append(int(input()))
print(sum(nums))
#     ```python
#     몇 번 입력받을래? (입력) 3
#     1
#     2
#     3
#     4
#     5
#     (출력) 15
#     ```
    

# 4. 리스트에서 짝수만 골라 새로운 리스트로 만들고 출력하시오.
lst = [1, 2, 3, 4, 5, 6]
evens = []
for n in lst:
    if n % 2 == 0:
        evens.append(n)
print(evens)
#     ```python
#     (입력) [1, 2, 3, 4, 5, 6]
#     (출력) [2, 4, 6]
#     ```
    

# 5. 리스트에서 최댓값과 최솟값의 차이를 출력하시오.
lst = [10, 2, 5, 8]
diff = max(lst) - min(lst)
print(diff)
#     ```python
#     (입력) [10, 2, 5, 8]
#     (출력) 8
#     ```
    

# 6. 정수들을 입력받아 짝수는 짝수끼리, 홀수는 홀수끼리 모아 두 개의 리스트로 나누어 출력하시오.
nums = list(map(int, input().split()))
even = []
odd = []
for n in nums:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print(even)
print(odd)
#     ```python
#     (입력) 1 2 3 4 5 6
#     (출력) [2, 4, 6] [1, 3, 5]
#     ```
    

# 7. 문자열을 입력받고 아래의 출력 양식으로 각 단어의 길이를 출력하시오.
words = input().split()
lengths = []
for word in words:
    if (word == words[-1]):
        print(len(word), end='')
        break
    print(len(word), end=', ')
#     ```python
#     (입력) hello world python
#     (출력) 5, 5, 6
#     ```
    

# 8. 리스트에서 값이 0인 요소의 개수를 구하시오.
lst = [0, 1, 0, 2, 3, 0]
print(lst.count(0))
#     ```python
#     (입력) [0, 1, 0, 2, 3, 0]
#     (출력) 3
#     ```
    

# 9. 정수들을 입력받아, 입력된 순서대로 누적합을 구하여 출력하시오.
nums = list(map(int, input().split()))
amount = []
total = 0
for num in nums:
    total += num
    amount.append(total)
print(amount)
#     ```python
#     (입력) 1 2 3 4
#     (출력) [1, 3, 6, 10]
#     ```
    
# 10. 리스트 `[1, 2, 3, 4, 5]`의 순서를 거꾸로 출력하시오.
lst = [1, 2, 3, 4, 5]
print(lst[::-1])
#     ```python
#     (입력) 없음
#     (출력) [5, 4, 3, 2, 1]
#     ```
    

# # 튜플

# 1. 튜플 `(10, 20, 30)`에서 두 번째 값을 출력하시오.
tpl = (10, 20, 30)
print(tpl[1])
#     ```python
#     (입력) 없음
#     (출력) 20
#     ```
    

# 2. 두 개의 튜플 `(1, 2)`와 `(3, 4)`를 연결하여 하나의 튜플로 만드시오.
tpl1 = (1, 2)
tpl2 = (3, 4)
print(tpl1 + tpl2)
#     ```python
#     (입력) 없음
#     (출력) (1, 2, 3, 4)
#     ```
    

# 3. 튜플에 저장된 값 중 최댓값과 최솟값을 출력하시오.
tpl = tuple(map(int, input().split()))
print(max(tpl))
print(min(tpl))
#     ```python
#     (입력) 7 2 9 4
#     (출력)
#     9
#     2
#     ```
    

# 4. 튜플에 저장된 값들의 평균을 소수 첫째 자리까지 출력하시오.
tpl = tuple(map(int, input().split()))
avg = sum(tpl) / len(tpl)
print("%.1f" % avg)
#     ```python
#     (입력) 10 20 30 40
#     (출력) 25.0
#     ```
    

# 5. 튜플에서 특정 값이 몇 번 등장하는지 세어 출력하시오.
nums = tuple(map(int, input().split()))
target = int(input("무슨 값을 셀까요? "))
print(nums.count(target))
#     ```python
#     (입력) 1 2 3 2 4 2
#     무슨 값을 셀까요? (입력) 2
#     (출력) 3
#     ```
    

# # 딕셔너리

# 1. 딕셔너리 `{"a": 1, "b": 2, "c": 3}`에서 키 `'b'`의 값을 출력하시오.
d = {"a": 1, "b": 2, "c": 3}
print(d["b"])
#     ```python
#     (입력) 없음
#     (출력) 2
#     ```
    

# 2. 빈 딕셔너리를 생성한 후, 키 `'x'`에 값 10을 추가하고 출력하시오.
d = {}
d['x'] = 10
print(d)
#     ```python
#     (입력) 없음
#     (출력) {'x': 10}
#     ```
    

# 3. name이 Alice고, age가 20인 딕셔너리에서 모든 키를 출력하시오.
d = {'name': 'Alice', 'age': 25}
print(d.keys())
#     ```python
#     (입력) 없음
#     (출력) dict_keys(['name', 'age'])
#     ```
    

# 4. name이 Alice고, age가 20인 딕셔너리에서 모든 값을 출력하시오.
d = {'name': 'Alice', 'age': 25}
print(d.values())
#     ```python
#     (입력) 없음
#     (출력) dict_values(['Alice', 25])
#     ```
    

# 5. 국어, 영어, 수학 점수를 딕셔너리로 입력받아 가장 높은 점수를 출력하시오.
kor, eng, math = map(int, input().split(', '))
scores = {'국어': kor, '영어': eng, '수학': math}
print(max(scores.values()))
#     ```python
#     (입력) 80, 90, 70
#     (출력) 90
#     ```
    

# 6. 사용자로부터 문자열을 입력받아 각 문자의 등장 횟수를 딕셔너리로 저장하고 출력하시오.
string = input()

d = {}
for s in string:
    d[s] = d.get(s, 0) + 1
    
print(d)
#     ```python
#     (입력) apple
#     (출력) {'a': 1, 'p': 2, 'l': 1, 'e': 1}
#     ```
    

# 7. 사용자로부터 학생 이름과 점수를 입력받아 딕셔너리를 만든 후 평균 점수를 출력하시오.
entries = input().split()

d = {}
for i in range(0, len(entries), 2):
    name = entries[i]
    score = int(entries[i+1])
    d[name] = score
    
avg = sum(d.values()) / len(d)

print(round(avg, 1))
#     ```python
#     (입력) Tom 70 Jerry 80 Genie 90
#     (출력) 80.0
#     ```
    

# 8. 과목 이름과 점수를 입력받아 딕셔너리에 저장한 뒤,
entries = input().split()

d = {}
for i in range(0, len(entries), 2):
    subject = entries[i]
    score = int(entries[i+1])
    d[subject] = score

for subject in d:
    score = d[subject]
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    if grade in ['A', 'B']:
        print(subject, end=' ')
#     점수를 기준으로 등급(A:90↑, B:80↑, C:70↑, D:60↑, F:그 외)을 매기고,
    
#     B등급 이상인 과목만 한 줄로 출력하시오.
    
#     ```python
#     (입력) math 95 english 83 history 72 art 59
#     (출력) math english
#     ```
    

# 9. 사용자로부터 과목을 입력받아 해당 키의 값을 출력하시오. 그런 과목이 존재하지 않으면 `"키 없음"`을 출력하시오.
d = {'수학': 90, '영어': 80}
key = input()
print(d.get(key, '키 없음'))
#     ```python
#     (입력) 수학
#     (출력) 90
#     ```
    
#     ```python
#     (입력) 실과
#     (출력) 90
#     ```
    

# 10. 사용자로부터 정수 쌍을 입력받아 딕셔너리를 생성하고 출력하시오.
nums = list(map(int, input().split()))

d = {}
for i in range(0, len(nums), 2):
    key = nums[i]
    value = nums[i+1]
    d[key] = value
    
print(d)
#     ```python
#     (입력) 3 300 2 400
#     (출력) {3: 300, 2: 400}
#     ```