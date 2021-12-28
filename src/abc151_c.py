class Item():
    def __init__(self, state, wrongCount):
        self.state = state
        self.wrongCount = wrongCount


N, M = map(int, input().split())
items = {}
pena = 0
correct = 0
for i in range(0, M):
    p, S = input().split()

    if p not in items:
        items[p] = Item("", 0)

    if items[p].state == "AC":
        continue

    if S == "AC":
        items[p].state = S
    else:
        pena = pena + 1
        items[p].state = S
        items[p].wrongCount = items[p].wrongCount + 1

items = {k: v for k, v in items.items() if v.state == "AC"}
print("{0} {1}".format(len(items), sum(v.wrongCount for v in items.values())))
