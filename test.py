n = int(input("입력: "))

# 상단 부분
for i in range(n):
    print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))

# 하단 부분
for i in range(1, n):
    print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))