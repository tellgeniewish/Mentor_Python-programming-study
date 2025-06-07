# 클래스

# 1. 정사각형(Square) 클래스에 한 변의 길이를 입력받아 넓이를 반환하는 `get_area()` 메서드를 정의하시오.
    
# ```python
# (출력) 넓이: 25
# ```

# ```python
class Square:
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length * self.length

sq = Square(5)
print("넓이: %d" % sq.get_area())
# ```
    

# 2. 자동차(Car) 클래스를 만들고, 생성자에서 색상과 속도를 초기화하여 출력하시오.
    
# ```bash
# (출력) 자동차 색상: 빨강, 속도: 100
# ```

# ```python
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

car1 = Car("빨강", 100)
print("자동차 색상: %s, 속도: %d" % (car1.color, car1.speed))
# ```
    

# **새 코드 짜기 귀찮으면 2번 문제 코드를 활용해도 됨**

# 3. Car 클래스를 사용하시오.
    
# 빨간 차와 파란 차가 있다.

# 생성된 인스턴스 수를 출력하시오.

# ```python
# (출력) 총 차량 수: 2
# ```

# ```python
class Car:
    count = 0

    def __init__(self, color):
        self.color = color
        Car.count += 1

car1 = Car("빨강")
car2 = Car("파랑")
print("총 차량 수: %d" % Car.count)
# ```
    

# 4. Car 클래스를 상속받은 SportsCar 클래스를 만들고, 속도를 200 이상 초과하지 않도록 `upSpeed()`를 오버라이딩하시오.
    
# ```bash
# (출력) 현재 속도(스포츠카): 200
# ```

# ```python
class Car:
    def __init__(self):
        self.speed = 0

    def upSpeed(self, value):
        self.speed += value

class SportsCar(Car):
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 200:
            self.speed = 200
        print("현재 속도(스포츠카): %d" % self.speed)

car = SportsCar()
car.upSpeed(250)
# ```
    

# 5. Student클래스를 사용해 `genie`와 `alex`의 중간(mid)과 기말(final) 점수를 각각 비교해서 **더 높은 점수를 가진 사람과 해당 점수**를 출력하는 코드를 작성하시오.
# - genie는 20살이고, alex는 23살이다.
# - genie의 mbti는 enfj이고, alex의 mbti는 esfj이다.
# - genie의 중간고사 점수는 95점, 기말고사 점수는 80점이다.
# - alex의 중간고사 점수는 60점, 기말고사 점수는 92점이다.

# ```python
# (출력) 안녕하세요, 제 이름은 genie이고, 나이는 20입니다
# genie의 mbti는? enfj입니다
# 안녕하세요, 제 이름은 alex이고, 나이는 23입니
# 다
# 현재 학생 수는? 2명 입니다
# 중간고사에서 더 높은 점수를 받은 사람은 genie이며, 점수는 95점입니다.
# 기말고사에서 더 높은 점수를 받은 사람은 alex이며, 점수는 92점입니다.
# 이제 나 죽습니다
# 이제 나 죽습니다
# ```

# ```python
class Student:
    name = ''
    mbti = ''
    age = 0
    count = 0
    mid_score = ''
    final_score= ''

    # 생성자: 반드시 존재 X
    def __init__(self, a, b, c, d, e):
        self.name = a
        self.mbti = b
        self.age = c
        self.mid_score = d
        self.final_score = e
        Student.count += 1 # 클래스 변수

    # 소멸자: 객체 소멸할 때 자동으로 호출됨
    def __del__(self): # self 꼭 써야 한다
        print("이제 나 죽습니다")

    def introduce(self):
        print("안녕하세요, 제 이름은 %s이고, 나이는 %d입니다" %(self.name, self.age))

# st1 = Student()
# st1.name = "suzy"
# st1.mbti = "enfp"
# st1.age = 20

st1 = Student("genie", "enfj", 20, 95, 80)

st1.introduce()
print("genie의 mbti는? %s입니다" %st1.mbti)

st2 = Student("alex", "esfj", 23, 60, 92)
st2.introduce()

print("현재 학생 수는? %d명 입니다" %st1.count) # st1.count 또는 st2.count 사용해도 ㄱㅊ
# Student.count 잘 안 씀

# 중간고사 비교
if st1.mid_score > st2.mid_score:
    print("중간고사에서 더 높은 점수를 받은 사람은 %s이며, 점수는 %d점입니다." % (st1.name, st1.mid_score))
elif st1.mid_score < st2.mid_score:
    print("중간고사에서 더 높은 점수를 받은 사람은 %s이며, 점수는 %d점입니다." % (st2.name, st2.mid_score))
else:
    print("중간고사 점수는 둘 다 %d점으로 같습니다." % st1.mid_score)

# 기말고사 비교
if st1.final_score > st2.final_score:
    print("기말고사에서 더 높은 점수를 받은 사람은 %s이며, 점수는 %d점입니다." % (st1.name, st1.final_score))
elif st1.final_score < st2.final_score:
    print("기말고사에서 더 높은 점수를 받은 사람은 %s이며, 점수는 %d점입니다." % (st2.name, st2.final_score))
else:
    print("기말고사 점수는 둘 다 %d점으로 같습니다." % st1.final_score)
# ```
    

# 6. 학생 클래스에 총점과 합격 여부를 판단하는 메서드를 추가하시오.
# Student 클래스를 정의하고, 이름과 중간/기말 점수를 생성자를 통해 초기화한 뒤, 총점을 계산하고 **총점이 160점 이상이면 합격, 그렇지 않으면 불합격**으로 출력하는 메서드를 작성하시오.
    
# ```bash
# (출력) 학생: genie, 총점: 170, 결과: 합격
# 학생: alex, 총점: 150, 결과: 불합격
# ```

# ```python
class Student:
    def __init__(self, name, mid_score, final_score):
        self.name = name
        self.mid_score = mid_score
        self.final_score = final_score

    def get_total(self):
        return self.mid_score + self.final_score

    def check_pass(self):
        total = self.get_total()
        if 160 <= total:
            result = "합격"
        else: "불합격"
        print("학생: %s, 총점: %d, 결과: %s" % (self.name, total, result))

st1 = Student("genie", 90, 80)
st2 = Student("alex", 80, 70)

st1.check_pass()
st2.check_pass()
# ```
    

# 7. 부모 클래스 Student를 상속받은 HighSchoolStudent 클래스를 정의하고, 성적에 따른 등급을 출력하시오.
    
# `Student` 클래스를 정의하고, 이름, 국어, 수학, 영어 점수를 초기화하도록 하시오.

# 이 클래스를 상속받은 `HighSchoolStudent` 클래스에서 `get_grade()` 메서드를 오버라이딩하여 **과목 평균**에 따라 다음 등급을 출력하시오:

# - 평균 90점 이상: A
# - 평균 80점 이상: B
# - 평균 70점 이상: C
# - 그 외: F

# ```python
# (출력) 학생: genie, 평균: 91.67, 등급: A
# 학생: alex, 평균: 78.33, 등급: C
# ```

# ```python
class Student:
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

    def get_average(self):
        return (self.korean + self.math + self.english) / 3

class HighSchoolStudent(Student):
    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        else:
            grade = "F"
        print("학생: %s, 평균: %.2f, 등급: %s" % (self.name, avg, grade))

# 객체 생성 및 테스트
st1 = HighSchoolStudent("genie", 95, 88, 92)
st2 = HighSchoolStudent("alex", 75, 80, 80)

st1.get_grade()
st2.get_grade()
# ```
    

# **7번 문제에서 바뀐 것은 파일 사용한다는 것 밖에 없음!**

# 8. 텍스트 파일로부터 학생 정보를 읽어와 HighSchoolStudent 클래스에서 평균과 등급을 출력하시오.
    
# 다음은 `student.txt` 파일

# ```python
# 이름,국어,수학,영어
# genie,95,88,92
# alex,75,80,80
# ```

# 다음은 출력 결과

# ```python
# (출력) 학생: genie, 평균: 91.67, 등급: A
# 학생: alex, 평균: 78.33, 등급: C
# ```

# ```python
class Student:
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

    def get_average(self):
        return (self.korean + self.math + self.english) / 3

class HighSchoolStudent(Student):
    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        else:
            grade = "F"
        print("학생: %s, 평균: %.2f, 등급: %s" % (self.name, avg, grade))

# 파일에서 학생 정보 읽기
with open("student.txt", 'r') as f:
    lines = f.readlines()[1:]
    
    for line in lines:
        name, kor, math, eng = line.strip().split(',')
        student = HighSchoolStudent(name, int(kor), int(math), int(eng))
        student.get_grade()
# ```
    

# ---

# 기말고사 대비

# 1. 1부터 100까지의 수 중에서 3의 배수이면서 5의 배수가 아닌 수의 개수를 구하시오.
    
# ```python
# (출력) 조건에 맞는 수의 개수: 27
# ```

# ```python
count = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        count += 1
print("조건에 맞는 수의 개수: %d" % count)
# ```
    

# 2. 상품 클래스와 파일을 활용하여 총 재고 수량을 구하시오.
# `Product` 클래스를 만들고, 이름과 수량을 받아 저장하시오.
# `products.txt` 파일에서 상품 정보를 읽고, 전체 재고 수량의 총합을 구하시오.
    
# ```python
# (파일 내용) keyboard,10
# mouse,15
# monitor,7
# ```

# 다음은 출력

# ```python
# (출력) 총 재고 수량: 32개
# ```

# ```python
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

total = 0
with open("products.txt", "r") as f:
    for line in f:
        name, qty = line.strip().split(',')
        item = Product(name, int(qty))
        total += item.quantity

print("총 재고 수량: %d개" % total)
# ```
    

# 3. 1부터 100까지 수 중에서 소수(prime number)만 출력하고 개수도 세시오.
    
# ```python
# (출력) 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
# 총 25개
# ```

# ```python
count = 0
for i in range(2, 101):
    is_prime = True
    for j in range(2, int(i)):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=' ')
        count += 1
print("\n총 %d개" % count)
# ```
    

# 4. 사용자로부터 숫자 여러 개를 한 줄에 입력받고(공백 구분), 가장 많이 등장한 숫자와 그 횟수를 출력하시오.
    
# ```python
# (입력) 5 1 3 5 3 5 2 1 1 3
# (출력) 가장 많이 나온 수: 5 (3회)
# ```

# ```python
nums = input().split()
count = {}

for n in nums:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

most = ''
max_count = 0

for k in count:
    if count[k] > max_count:
        most = k
        max_count = count[k]

print("가장 많이 나온 수: %s (%d회)" % (most, max_count))
# ```
    

# 5. 문장에서 각 단어의 등장 횟수를 세고 사전 순으로 출력하시오.
# 사용자로부터 문자열 한 줄을 입력받아, 각 단어가 **몇 번 등장했는지** 출력하시오.
# 출력은 **단어를 오름차순(사전순)으로 정렬해서** 보여줄 것.
    
# ```python
# (입력) apple banana apple orange banana apple
# (출력) apple: 3
# banana: 2
# orange: 1
# ```

# ```python
sentence = input()
words = sentence.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word in sorted(count):
    print("%s: %d" % (word, count[word]))

# 또는 아래 방법으로
# words = list(count.keys())  # 딕셔너리 키를 리스트로 변환
# words.sort()  # 리스트니까 가능
# for word in words:
#     print("%s: %d" % (word, count[word]))
# ```
    

# 6. 사용자로부터 숫자를 계속 입력받아 합계와 평균을 출력하시오.
    
# 사용자에게 정수를 계속 입력받는다.

# - 양수는 모두 더한다.
# - **음수가 입력되면 즉시 입력을 종료**하고,
#     - **입력한 수의 개수** (음수 제외)
#     - **총합**
#     - **평균** (소수 둘째 자리까지)

# 를 출력하시오.

# ```python
# (입력) 10  
# 20  
# 30  
# -1
# (출력) 입력한 수의 개수: 3
# 총합: 60
# 평균: 20.00
# ```

# ```python
# (입력) -1
# (출력) 입력한 수의 개수: 0
# 총합: 0
# 평균: 계산할 수 없음
# ```

# ```python
count = 0
total = 0

while True:
    n = int(input())
    if n < 0:
        break
    total += n
    count += 1

print("입력한 수의 개수: %d" % count)
print("총합: %d" % total)

if count > 0:
    avg = total / count
    print("평균: %.2f" % avg)
else:
    print("평균: 계산할 수 없음")
# ```