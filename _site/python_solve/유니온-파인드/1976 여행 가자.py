# 부모 찾기.
def getParent(parent, c):
    if parent[c] == c: return c
    parent[c] = getParent(parent, parent[c])
    return parent[c]

# 합집합.
def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a < b: parent[b] = a
    else: parent[a] = b

# 부모 찾기.
def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a == b: return 1
    else: return 0

if __name__ == "__main__":
    # 도시와 여행할 도시 수.
    n = int(input())
    m = int(input())
    # 연결된 도시 설정.
    location = list()

    # 연결된 도시 알아내기.
    for i in range(n):
        s = list(map(int,input().split()))
        for j in range(n):
            if s[j] == 1:
                if (i+1, j+1) not in location and (j+1, i+1) not in location:
                    location.append((i+1,j+1))

    # 여행 도시.
    trip = list(map(int,input().split()))

    # 부모 노드 설정.
    parent = [int(i) for i in range(n+1)]

    # 저장한 연결된 도시를 합집합으로 만들어준다.
    for i in location:
        unionParent(parent, i[0], i[1])

    count = 0
    # 모두 연결되어있으므로, 첫번째와 마지막 도시의 부무노드는 무조건 같아야한다.
    parent_num = findParent(parent, trip[0], trip[-1])
    # 찾은 부모노드를 이용해서, 여행해야하는 도시와 찾은 부모노드끼리 부모를 찾고, 환
    # 일치하면, 1을 반환 그렇지 않으면 0을 반환한다. 그리고 count에 더해준다.
    for i in trip:
        count += findParent(parent, parent_num, i)

    # 도시 만큼 돌고 찾은 부모가 같을경우 1을 반환해주는데, 여행 경로만큼 count가 되어야한다.
    # 그래야 여행가능하다는것이다.
    if count == len(trip): print("YES")
    else: print("NO")