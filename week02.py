# 1. 1부터 10까지 출력하는 코드를 작성하시오.
for i in range(1, 11):
    print("%d" % i, end=' ')
#     ```python
#     1 2 3 4 5 6 7 8 9 10
#     ```
    

# 2. 1부터 N까지 출력하는 코드를 작성하시오.
n = int(input())
for i in range(1, n + 1):
    print("%d" % i)
#     ```python
#     (입력)5
#     1
#     2
#     3
#     4
#     5
#     ```
    
#     ```python
#     (입력)3
#     1
#     2
#     3
#     ```
    

# 3. 1부터 N까지 짝수만 출력하는 코드를 작성하시오.
n = int(input())
for i in range(2, n + 1, 2):
    print("%d" % i)
#     ```python
#     (입력)7
#     2
#     4
#     6
#     ```
    

# 4. N의 구구단 출력하는 코드를 작성하시오.
n = int(input())
for i in range(1, 10):
    print("%d x %d = %d" % (n, i, n * i))
#     ```python
#     (입력)3
#     3 x 1 = 3
#     3 x 2 = 6
#     3 x 3 = 9
#     3 x 4 = 12
#     3 x 5 = 15
#     3 x 6 = 18
#     3 x 7 = 21
#     3 x 8 = 24
#     3 x 9 = 27
#     ```
    

# 5. 사용자가 입력한 숫자 N까지의 합을 구하는 코드를 작성하시오.
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print("합: %d" % sum)
#     ```python
#     (입력)5
#     합: 15
#     ```
    
#     ```python
#     (입력)3
#     합: 6
#     ```
    

# 6. 구구단 2단을 출력하는 코드를 작성하시오.
for i in range(1, 10):
    print("2 * %d = %d" % (i, 2 * i))
#     ```python
#     2 * 1 = 2
#     2 * 2 = 4
#     ...
#     2 * 9 = 18
#     ```
    

# 7. 사용자가 입력한 정수 N의 약수를 출력하는 코드를 작성하시오
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print("%d" % i)
#     ```python
#     (입력)6
#     1
#     2
#     3
#     6
#     ```
    
#     ```python
#     (입력)10
#     1
#     2
#     5
#     10
#     ```
    
# 8. 사용자가 입력한 두 수 A, B 사이의 모든 정수를 출력하는 코드를 작성하시오.
a, b = map(int, input().split())
for i in range(a, b + 1):
    print("%d" % i)
#     ```python
#     (입력)3 7
#     3
#     4
#     5
#     6
#     7
#     ```
    
#     ```python
#     (입력)10 15
#     10
#     11
#     12
#     13
#     14
#     15
#     ```
    

# 9. 1부터 100까지의 숫자 중 3의 배수만 출력하는 코드를 작성하시오.
for i in range(3, 101, 3):
    print("%d" % i)
#     ```python
#     3
#     6
#     9
#     ...
#     99
#     ```
    

# 10. 사용자가 입력한 숫자 N의 팩토리얼을 계산하는 코드를 작성하시오.
    
#     `n! = n × (n-1) × (n-2) × ... × 1`
    
#     `3!`는 `3 × 2 × 1 = 6`
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print("%d" % fact)
#     ```python
#     (입력)5
#     120
#     ```
    

# 11. 별(*)을 이용하여 높이가 N인 직각삼각형을 출력하는 코드를 작성하시오.
n = int(input())
for i in range(1, n + 1):
    print("%s" % ('*' * i))
#     ```python
#     (입력)3
#     *
#     **
#     ***
#     ```
    

# 12. 구구단 2단의 다음 출력문을 만드는 코드를 작성하시오.
for i in range(1, 6):
    print("2 * %d = %d" % (i, 2 * i), end=' ')
    if i + 5 != 10:
        print("2 * %d = %d" % (i + 5, 2 * (i + 5)))
    else:
        print() # 줄바꿈만 출력
#     ```python
#     2 * 1 = 2 2 * 6 = 12
#     2 * 2 = 4 2 * 7 = 14
#     2 * 3 = 6 2 * 8 = 16
#     2 * 4 = 8 2 * 9 = 18
#     2 * 5 = 10
#     ```
    

# 13. 사용자가 입력한 문자열이 팰린드롬인지 확인하는 코드를 작성하시오.
    
#     (팰린드롬: 앞에서 읽으나 뒤에서 읽으나 같은 문자열)
s = input()
if s == s[::-1]:
    print("YES")
else:
    print("NO")
-----
s = input("")
length = len(s)
flag = False
for i in range(length // 2):
    if s[i] != s[length - i - 1]:
        break
else:
    flag = True

if flag:
    print("YES")
else:
    print("NO")
#     ```python
#     level
#     YES
#     ```
    
#     ```python
#     hello
#     NO
#     ```
    

# 14. 사용자가 입력한 정수 N에 대해, 아래와 같은 형태의 별(*)을 출력하는 코드를 작성하시오.
n = int(input())
for i in range(n):
    print("%s%s" % (' ' * (n - i - 1), '*' * (2 * i + 1)))
#     ```python
#     (입력)5
#         *
#        ***
#       *****
#      *******
#     *********
#     ```
    

# 15. 사용자가 입력한 정수 N에 대해, 아래와 같은 형태의 별(*)을 출력하는 코드를 작성하시오.
n = int(input())

# 상단 모래시계 부분
for i in range(n):
    print(" " * i + "*" * (2 * (n - i) - 1))

# 하단 모래시계 부분
for i in range(1, n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
#     ```python
#     (입력)5
#     *********
#      *******
#       *****
#        ***
#         *
#        ***
#       *****
#      *******
#     *********
#     ```
    

# 16. 사용자가 입력한 정수 N에 대해, 아래와 같은 형태의 별(*)을 출력하는 코드를 작성하시오.
n = int(input())

# 상단 부분
for i in range(n):
    print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))

# 하단 부분
for i in range(1, n):
    print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))
#     ```python
#     (입력)5
#     *        *
#     **      **
#     ***    ***
#     ****  ****
#     **********
#     ****  ****
#     ***    ***
#     **      **
#     *        *
#     ```