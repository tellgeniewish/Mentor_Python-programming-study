words = input().split()
result = []
for w in words:
    # 첫 문자와 마지막 문자를 소문자로 비교
    if w[0].lower() == w[-1].lower():
        result.append(w.title())
# 결과를 쉼표로 연결하여 한 줄로 출력
print(', '.join(result))
