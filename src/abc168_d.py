from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def main():
    N, M = map(int, input().split())
    dic = {}
    for i in range(1, N + 1):
        dic[i] = Node(i)
    for i in range(0, M):
        A, B = map(int, input().split())
        dic[A].children.append(dic[B])
        dic[B].children.append(dic[A])

    answerDic = {}
    q = deque()
    q.append(dic[1])
    while len(q) > 0:
        current = q.popleft()
        for child in current.children:
            if child.data not in answerDic.keys() :
                answerDic[child.data] = current.data
                q.append(child)

    print('Yes')
    for key in range(2, N + 1):
        print(answerDic[key])

if __name__ == "__main__":
    main()