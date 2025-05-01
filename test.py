def who_is_pass(scores):
    for i in range(scores):
        if scores[i] >= 60:
            print(i + 1, end=' ')

scores = list(map(int, input().split()))
who_is_pass(scores)