a, b, c = map(int, input("세 정수를 입력하세요: ").split())

if a == 0 or b == 0 or c == 0:
    print("0은 포함될 수 없습니다.")
elif a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print("모두 짝수입니다.")
elif a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
    print("모두 홀수입니다.")
else:
    print("홀수와 짝수가 섞여 있습니다.")