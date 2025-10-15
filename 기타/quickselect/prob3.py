import csv  # csv 파일을 처리하는 함수를 지원
import time # 알고리즘 수행 시간을 측정하기 위해 필요
# csv, time 이외에 다른 라이브러리를 사용하지 않습니다.

# read input files 
table = [] # 날씨에 대한 데이터를 저장하는 리스트

startTime = time.time() # 측정 시작

for i in range(2001,2026): # 각 년도마다 파일이 있음
    filename = str(i) + ".csv" # 읽어 드릴 csv 파일 이름을 만듦
    f = open(filename,'r', encoding='cp949')  # 파일을 오픈
    rdr = csv.reader(f) # 파일 포인터를 생성
    next(rdr) # 헤더 건너뛰기

######################################################################################
# TO DO : 이 지점부터 수강생의 코딩을 시작함
# 학번 : 202210587
# 이름 : 정선연

    for line in rdr:
        try: # null값 처럼 치수로 변환할 수 없는 값이 있을 수 있으므로 예외 처리
            temperature = float(line[2])  # 기온 3번째 컬럼을 float로 변환 시도
            speed = float(line[4])  # 풍속 5번째 컬럼을 float로 변환 시도
            speed_km = speed * 3.6 # km/h 변환
            
            V016 = (speed_km ** 0.16) if speed_km > 0 else 0.0
            wind = 13.12 + 0.6215*temperature - 11.37*V016 + 0.3965*temperature*V016  # 체감온도(°C)

            row = [i,line[1],wind] # 연도, 측정일시, 체감온도가 하나의 행으로 저장됨
            table.append(row) # 변환된 데이터를 table에 추가
        except ValueError: # 변환할 수 없는 값이 있어 값 오류
            continue  # 해당 행은 건너뜀
    f.close() # 파일을 닫음

"""
Quickselect로 k번째 체감온도와 해당 일시/연도 find
"""
def quickselect_kth(records, k):
    # [year, datetime, wind_chill]
    arr = [[r[2], r[0], r[1]] for r in records]  # [value, year, datetime]
    lo, hi = 0, len(arr) - 1

    def partition(l, r):
        pivot = arr[(l + r) // 2][0]
        i, j = l - 1, r + 1
        while True:
            i += 1
            while arr[i][0] < pivot:
                i += 1
            j -= 1
            while arr[j][0] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    while lo < hi:
        p = partition(lo, hi)
        if k <= p:
            hi = p
        else:
            lo = p + 1
    # (year, datetime, value)
    return (arr[lo][1], arr[lo][2], arr[lo][0])

# Nearest-Rank 인덱스(ceil(p*n) → 0-based)
def nearest_rank_index(p, n):
    r = int(p * n)
    if p * n != r:
        r += 1
    if r < 1: r = 1
    if r > n: r = n
    return r - 1

total_n = len(table)
if total_n == 0:
    print("데이터가 없습니다.")
    with open("prob3-result.csv", "w", newline='', encoding="cp949") as f:
        csv.writer(f).writerow(["연도","<25% 개수",">75% 개수","행 개수","<25% 비율",">75% 비율"])
    raise SystemExit

k25 = nearest_rank_index(0.25, total_n)
k75 = nearest_rank_index(0.75, total_n)

# 실제 25%, 75% 원소 선택
N25 = quickselect_kth(table, k25)   # (year, datetime, value)
N75 = quickselect_kth(table, k75)

# 콘솔 출력
print("25% 일시:" + N25[1] + " 체감온도:" + str(round(N25[2], 5)))
print("75% 일시:" + N75[1] + " 체감온도:" + str(round(N75[2], 5)))
endTime = time.time()
print("수행시간:" + str(endTime - startTime))

# 연도별 <25%, >75% 카운트
q25, q75 = N25[2], N75[2]
# ctr: [연도, <25% 개수, >75% 개수, 행 개수, <25% 비율, >75% 비율]
ctr = [[year, 0, 0, 0, 0.0, 0.0] for year in range(2001, 2026)]

def yidx(y): return y - 2001  # 2001→0 ... 2025→24

for y, dt, wc in table:
    j = yidx(y)
    ctr[j][3] += 1                 # 전체 행 수
    if wc < q25:
        ctr[j][1] += 1             # <25% 개수
    if wc > q75:
        ctr[j][2] += 1             # >75% 개수

# 비율 계산
for row in ctr:
    total = row[3]
    if total > 0:
        row[4] = row[1] / total
        row[5] = row[2] / total

# ctr 테이블에 각 연도별 계산된 데이터가 들어 있다고 가정
ctr[0] = ["연도","<25% 개수",">75% 개수","행 개수","<25% 비율",">75% 비율"]
# write output file
f = open("prob3-result.csv",'w',newline='')
wdr = csv.writer(f)
wdr.writerows(ctr)
f.close()
