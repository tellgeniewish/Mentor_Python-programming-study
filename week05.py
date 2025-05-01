# 1. 두 수를 전달받아 합을 반환하는 함수를 정의하시오.

# ```python
# (입력) 두 수를 입력하세요: 3 5
# (출력) 8
# ```

# ```python
def add(a, b):
    return a + b

x, y = map(int, input("두 수를 입력하세요: ").split())
print(add(x, y))
# ```

# 2. 문자열을 입력받아 대문자로 변환하는 함수를 정의하고 실행하시오.

# ```python
# (입력) python
# (출력) PYTHON
# ```

# ```python
def to_upper(s):
    return s.upper()

s = input()
print(to_upper(s))
# ```

# 3. 리스트의 길이를 반환하는 함수를 정의하시오.

# ```python
# (입력) 1 2 3 4
# (출력) 4
# ```

# ```python
def list_length(lst):
    return len(lst)

lst = list(map(int, input().split()))
print(list_length(lst))
# ```


# 4. 문자열을 입력받아 맨 앞 글자와 맨 뒤 글자가 같은지 확인하는 함수를 정의하시오.

# ```python
# (입력) level
# (출력) True
# ```

# ```python
def is_same_ends(s):
    return s[0] == s[-1]

s = input()
print(is_same_ends(s))
# ```


# 5. 정수 리스트에서 짝수만 골라 새로운 리스트로 반환하는 함수를 정의하시오.

# ```python
# (입력) 1 2 3 4 5 6
# (출력) [2, 4, 6]
# ```

# ```python
def get_even(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x)
    return result

nums = list(map(int, input().split()))
print(get_even(nums))
# ```


# 6. 문자열에서 공백을 제거하고 소문자로 바꿔주는 함수를 정의하시오.

# ```python
# (입력) Hello World
# (출력) helloworld
# ```

# ```python
def clean_string(s):
    return s.replace(" ", "").lower()

s = input()
print(clean_string(s))
# ```


# 7. 두 수를 전달받아 큰 값을 반환하는 함수를 정의하시오.

# ```python
# (입력) 7 10
# (출력) 10
# ```

# ```python
def bigger(a, b):
    if a > b:
        return a
    else:
        return b

x, y = map(int, input().split())
print(bigger(x, y))
# ```


# 8. 리스트에서 가장 많이 나온 숫자를 찾아 반환하는 함수를 정의하시오.

# ```python
# (입력) 1 2 2 3 2 4
# (출력) 2
# ```

# ```python
def most_common(lst):
    max_count = 0
    result = None
    for x in lst:
        if lst.count(x) > max_count:
            max_count = lst.count(x)
            result = x
    return result

nums = list(map(int, input().split()))
print(most_common(nums))
# ```


# 9. 문자열 리스트에서 길이가 3 이상인 문자열만 골라 반환하는 함수를 정의하시오.

# ```python
# (입력) a bb cat apple
# (출력) ['cat', 'apple']
# ```

# ```python
def filter_length(words):
    result = []
    for w in words:
        if len(w) >= 3:
            result.append(w)
    return result

words = input().split()
print(filter_length(words))
# ```


# 10. 세 개의 정수를 전달받아 가장 큰 수를 반환하는 함수를 정의하시오.

# ```python
# (입력) 10 25 15
# (출력) 25
# ```

# ```python
def max_of_three(a, b, c):
    three = [a, b, c]
    max_val = max(three)
    return max_val

a, b, c = map(int, input().split())
print(max_of_three(a, b, c))
# ```


# 11. 문자열을 전달받아, 알파벳이 아닌 문자를 제거한 뒤 소문자로 반환하는 함수를 정의하시오.

# ```python
# (입력) Hello! 123 World.
# (출력) helloworld
# ```

# ```python
def clean_alpha(s):
    result = ''
    for ch in s:
        if ch.isalpha():
            result += ch.lower()
    return result

s = input()
print(clean_alpha(s))
# ```


# 12. 정수 n을 입력받아 1부터 n까지 합을 구하는 함수를 정의하시오.

# ```python
# (입력) 5
# (출력) 15
# ```

# ```python
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input())
print(sum_to_n(n))
# ```


# 13. 문자열 리스트를 입력받아, 각 문자열의 길이를 원소로 가지는 리스트를 반환하시오.

# ```python
# (입력) hi hello python
# (출력) [2, 5, 6]
# ```

# ```python
def length_list(words):
    result = []
    for w in words:
        result.append(len(w))
    return result

words = input().split()
print(length_list(words))
# ```


# 14. 숫자 리스트를 받아 짝수의 개수와 홀수의 개수를 튜플로 반환하는 함수를 정의하시오.

# ```python
# (입력) 1 2 3 4 5 6
# (출력) (3, 3)
# ```

# ```python
def count_even_odd(lst):
    even = 0
    odd = 0
    for x in lst:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

nums = list(map(int, input().split()))
print(count_even_odd(nums))
# ```


# 15. 문자열을 받아 단어별로 분리한 뒤, 각 단어의 첫 글자만 이어붙인 문자열을 반환하는 함수를 정의하시오.

# ```python
# (입력) Data Science
# (출력) DS
# ```

# ```python
def initials(s):
    words = s.split()
    result = ''
    for w in words:
        result += w[0].upper()
    return result

s = input()
print(initials(s))
# ```


# 16. 학생들의 점수가 주어진 리스트에서 합격자만 출력하는 함수를 작성하시오. 점수 리스트에서 60점 이상인 학생의 번호(1번부터 시작)를 출력하는 함수 `print_passed_students`를 정의하시오. 리스트에는 10명의 학생 점수가 주어지며, 합격자는 점수 60점 이상인 학생들이다.(단, 학생 번호는 1번부터 시작)

# ```python
# (입력) 50 72 80 45 60 90 56 67 88 40
# (출력) 2 3 5 6 8 9
# ```

# ```python
def who_is_pass(scores):
    for i in range(len(scores)):
        if scores[i] >= 60:
            print(i + 1, end=' ')

scores = list(map(int, input().split()))
who_is_pass(scores)
# ```


# 17. 문자열을 입력받아 각 문자가 몇 번 나왔는지 딕셔너리로 반환하는 함수를 정의하시오.

# ```python
# (입력) banana
# (출력) {'b': 1, 'a': 3, 'n': 2}
# ```

# ```python
def char_count(s):
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d

s = input()
print(char_count(s))
# ```


# 18. 정수 n을 입력받아, n의 약수를 모두 리스트로 반환하는 함수를 정의하시오.

# ```python
# (입력) 12
# (출력) [1, 2, 3, 4, 6, 12]
# ```

# ```python
def get_divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

n = int(input())
print(get_divisors(n))
# ```


# 19. 문자열을 입력받아, 공백을 기준으로 나눈 단어 중 가장 긴 단어를 반환하시오.

# ```python
# (입력) I love programming in Python
# (출력) programming
# ```

# ```python
def longest_word(s):
    words = s.split()
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

s = input()
print(longest_word(s))
# ```


# 20. 문자열과 문자를 입력받아, 해당 문자가 처음 등장하는 위치를 반환하시오. 만약 존재하지 않으면 `'없음'`을 반환하시오.

# ```python
# (입력) programming
# (입력) g
# (출력) 3
# ```

# ```python
def find_char(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            return i
    return '없음'

s = input()
ch = input()
print(find_char(s, ch))
# ```