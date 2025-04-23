# 1. 문자열 `"hello"`와 리스트 `['h', 'e', 'l', 'l', 'o']`를 비교하면 같은지 확인하시오.
s = "hello"
l = ['h', 'e', 'l', 'l', 'o']

print(s == l)
#     ```python
#     (입력) 없음  
#     (출력) False
#     ```
    
# 2. 문자열 `"abc"`에 `"123"`을 덧셈 연산자로 이어 붙이고 출력하시오.
s = "abc"
print(s + "123")
#     ```python
#     (입력) 없음  
#     (출력) abc123
#     ```
    

# 3. 문자열 `"ha"`를 3번 곱해서 출력하시오.
print("ha" * 3)
#     ```python
#     (입력) 없음  
#     (출력) hahaha
#     ```
    

# 4. 입력받은 문자열의 길이를 출력하시오.
s = input()
print(len(s))
#     ```python
#     (입력) Python
#     (출력) 6
#     ```
    

# 5. 문자열 `"hello"`를 대문자로 바꾸어 출력하시오.
print("hello".upper())
#     ```python
#     (입력) 없음  
#     (출력) HELLO
#     ```
    

# 6. `"Python Is Fun"` 문자열의 대소문자를 서로 바꿔 출력하시오.
print("Python Is Fun".swapcase())
#     ```python
#     (입력) 없음  
#     (출력) pYTHON iS fUN
#     ```
    

# 7. 문자열 `"welcome to my place"`을 제목 형태로 바꿔 출력하시오.
print("welcome to my place".title())
#     ```python
#     (입력) 없음  
#     (출력) Welcome To My Place
#     ```
    

# 8. 입력받은 문자열이 모두 소문자/대문자/숫자인지 확인하시오.
s = input()

if s.isupper():
    print("대문자입니다.")
elif s.islower():
    print("소문자입니다.")
elif s.isdigit():
    print("숫자입니다.")
#     ```python
#     (입력) abc
#     (출력) 소문자입니다.
#     ```
    
#     ```python
#     (입력) HELLO
#     (출력) 대문자입니다.
#     ```
    
#     ```python
#     (입력) HELLO
#     (출력) 숫자입니다.
#     ```
    

# 9. `"banana"`에서 `'a'`의 개수를 출력하시오.
print("banana".count('a'))
#     ```python
#     (입력) 없음  
#     (출력) 3
#     ```
    

# 10. `"hello world"`에서 `'o'`의 첫 번째와 마지막 인덱스를 출력하시오.
print("o의 첫 번째 인덱스는 ", "hello world".find('o'), "이고, 마지막 인덱스는 ", "hello world".rfind('o'), "입니다.", sep='')
#     ```python
#     (입력) 없음  
#     (출력) o의 첫 번째 인덱스는 4이고, 마지막 인덱스는 7입니다.
#     ```
    

# 11. `"a,b,c"`를 쉼표를 기준으로 나누어 리스트로 출력하시오.
print("a,b,c".split(','))
#     ```python
#     (입력) 없음  
#     (출력) ['a', 'b', 'c']
#     ```
    

# 12. 리스트 `['hi', 'i\'m', 'genie']`를 공백으로 연결된 문자열로 만들어 출력하시오.
print(" ".join(['hi', 'i\'m', 'genie']))
#     ```python
#     (입력) 없음  
#     (출력) hi i'm genie
#     ```
    

# 13. `"  hello  world  "` 문자열에서 양쪽 공백만 제거하고, `"hello  world"` 문자열을 출력하시오. 가운데 공백은 유지되어야 함.
s = "  hello  world  "
print(s.strip())
#     ```python
#     (입력) 없음  
#     (출력) hello  world
#     ```
    

# 14. 사용자로부터 입력받은 문자열에서 `'@'`가 **두 번 이상** 등장할 경우 두 번째 `'@'`의 인덱스를 출력하시오. 단, 그렇지 않으면 `"없음"`을 출력하시오.
s = input()

first = s.find("@")
second = s.find("@", first + 1)
if second == -1:
    print("없음")
else: print(second)
#     ```python
#     (입력) abc@def@ghi
#     (출력) 7
#     ```
    
#     ```python
#     (입력) 12345
#     (출력) 없음
#     ```
    

# 15. 문자열 `"###data#science###"`에서 좌우 양쪽에 있는 `'#'` 기호를 모두 제거하고 `"data#science"`를 출력하시오. 가운데의 `'#'`는 유지되어야 함.
print("###data#science###".strip('#'))
#     ```python
#     (입력) 없음  
#     (출력) data#science
#     ```
    

# 16. 문자열에서 공백을 제거한 후 `'a'`가 등장하는 위치를 모두 출력하시오.
s = input().replace(" ", "")
index = s.find('a')

while index != -1:
    print(index, end=' ')
    index = s.find('a', index + 1)
#     ```python
#     (입력)     banana  boat
#     (출력) 1 3 5 8
#     ```
    

# 17. 문자열에서 맨 앞과 맨 뒤의 공백 수를 각각 출력하시오.
    
#     (hi 앞에 한 칸 띄우고, hello 뒤에 5칸 띄움)
s = input()

left = len(s) - len(s.lstrip())
right = len(s) - len(s.rstrip())
print(left, right)
#     ```python
#     (입력)  hi hello         
#     (출력) 1 5
#     ```
    

# 18. 이메일을 입력하고,  `'@'` 다음에 오는 첫 글자를 출력하시오. (단, '@'가 문자열에 반드시 포함됨)
email = input()
idx = email.index('@')
print(email[idx+1])
#     ```python
#     (입력) user@example.com
#     (출력) e
#     ```
    

# 19. 입력받은 문자열의 양 끝 문자가 같은지 비교하여 출력하시오.
s = input().strip()
print(s[0] == s[-1])
#     ```python
#     (입력) abcba
#     (출력) True
#     ```
    
#     ```python
#     (입력) 12321
#     (출력) True
#     ```
    
#     ```python
#     (입력) 123
#     (출력) False
#     ```
    

# 20. 공백으로 구분된 단어들을 입력받아, 각 단어의 첫 문자와 마지막 문자가 같으면 해당 단어를 제목 형태로 변환한 뒤 리스트에 저장하고, 최종적으로 쉼표(`,`)로 연결하여 출력하시오.
words = input().split()

result = []
for w in words:
    if w[0].lower() == w[-1].lower():
        result.append(w.title())

print(', '.join(result))
#     ```python
#     (입력) level Test radar apple
#     (출력) Level, Test, Radar
#     ```