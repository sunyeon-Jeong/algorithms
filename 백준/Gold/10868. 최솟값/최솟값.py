# 세그먼트 트리
# 시간복잡도 O((N+M) log N)

import sys
input = sys.stdin.readline

# N : 데이터개수, M : 질의개수
sizeN, queryCnt = map(int, input().split())
data = [int(input()) for _ in range(sizeN)]

# 트리크기 계산 : N 이상이 되는 가장 가까운 2거듭제곱
tree_size = 1
while tree_size < sizeN:
    tree_size *= 2

# 입력값 상한보다 큰 값
INF = 10**10
tree = [INF] * (2 * tree_size)

# 리프노드
for i in range(sizeN):
    tree[tree_size + i] = data[i]
    
# 내부노드 계산 : 각 구간 최소값
for i in range(tree_size - 1, 0, -1):
    tree[i] = min(tree[i * 2], tree[i * 2 + 1])
    
def query_min(left, right):
    # 구간 최소값
    left += tree_size - 1
    right += tree_size - 1
    min_value = INF
    
    while left <= right:
        if left % 2 == 1:
            min_value = min(min_value, tree[left])
            left += 1
        if right % 2 == 0:
            min_value = min(min_value, tree[right])
            right -= 1
        left //= 2; right //= 2
        
    return min_value

for _ in range(queryCnt):
    queryLeft, queryRight = map(int, input().split())
    print(query_min(queryLeft, queryRight))