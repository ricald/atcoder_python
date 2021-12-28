import collections

N = int(input())

S = []
for i in range(0, N):
    S.append(input())

c = collections.Counter(S)
max = max(c.values())
answerlist = [key for key, v in c.items() if v == max]
answerlist.sort()
for answer in answerlist:
    print(answer)
