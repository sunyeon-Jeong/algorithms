# 분할정복기반 선택 알고리즘 (재귀X)
# 시간복잡도 평균 O(N)

import sys
input = sys.stdin.readline

n, kth = map(int, input().split())
arr = list(map(int, input().split()))
target = kth - 1

# 오른쪽 파티션의 마지막 인덱스 반환
def hoare_partition(lo: int, hi: int) -> int:
    pivot = arr[(lo + hi) // 2]
    i, j = lo - 1, hi + 1
    
    while True:
        # pivot 보다 작은 원소를 찾을 때까지 increase
        i += 1
        while arr[i] < pivot:
            i += 1
        # pivot 보다 큰 원소를 찾을 때까지 decrease
        j -= 1
        while arr[j] > pivot:
            j -= 1
        # 포인터 교차 -> 경계반환
        if i >= j:
            return j
        # 두 원소 교환
        arr[i], arr[j] = arr[j], arr[i]

# 반복형 quickselect
lo, hi = 0, n - 1

while lo < hi:
    mid = hoare_partition(lo, hi)
    if target <= mid:
        hi = mid
    else:
        lo = mid + 1

print(arr[lo])