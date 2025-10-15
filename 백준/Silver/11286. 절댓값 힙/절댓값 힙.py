# 시간복잡도 O(log N)
import sys
import heapq

input = sys.stdin.readline

# (abs(value), value) 튜플로 저장
operation_cnt = int(input().strip())
abs_heap = []

for _ in range(operation_cnt):
    value = int(input().strip())

    if value != 0:
        # 삽입 : (절댓값, 실제값) 튜플
        heapq.heappush(abs_heap, (abs(value), value))
    else:
        # 삭제 : 비어있으면 0, 아니면 최상단 pop
        if not abs_heap:
            print(0)
        else:
            _, chosen = heapq.heappop(abs_heap)
            print(chosen)
