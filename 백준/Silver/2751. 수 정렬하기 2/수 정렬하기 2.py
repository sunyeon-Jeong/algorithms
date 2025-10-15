# 병합정렬
# 시간복잡도 O(N log N)
import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
temp = [0] * n

# 병합정렬 정렬
def merge_sort(left, right):
    if right - left <= 1:
        return
    
    mid = (left + right) // 2
    merge_sort(left, mid)
    merge_sort(mid, right)
    
    # 병합
    i, j, k = left, mid, left
    while i < mid and j < right:
        if nums[i] < nums[j]:
            temp[k] = nums[i]
            i += 1
        else:
            temp[k] = nums[j]
            j += 1
        k += 1
        
    # 나머지 값 복사
    while i < mid:
        temp[k] = nums[i]
        i += 1; k += 1
    while j < right:
        temp[k] = nums[j]
        j += 1; k += 1
        
    # 원본배열에 복사
    for index in range(left, right):
        nums[index] = temp[index]

merge_sort(0, n)

sys.stdout.write('\n'.join(map(str, nums)) + '\n')