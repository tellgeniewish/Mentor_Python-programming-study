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