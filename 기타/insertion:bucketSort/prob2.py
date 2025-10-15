import csv  # csv 파일을 처리하는 함수를 지원
import time # 알고리즘 수행 시간을 측정하기 위해 필요
import random # 데이터를 임의로 섞기 위해 필요
# csv, time, random 이외에 다른 라이브러리를 사용하지 않음 

# read input files 
table = []  # 인체 치수에 대한 데이터를 저장하는 리스트
for i in [4,5,8]: # 파일이 총 세 개가 있음
    filename = str(i) + "rd.csv"  # 읽어 드릴 csv 파일 이름을 만듦
    f = open(filename,'r', encoding='cp949')  # 파일을 오픈
    rdr = csv.reader(f) # 파일 포인터를 생성
    for line in rdr:
        try: # null값 처럼 치수로 변환할 수 없는 값이 있을 수 있으므로 예외 처리
            height = float(line[3])  # 키 값이 있는 4번째 컬럼(키)를 float로 변환 시도
            weight = float(line[4])  # 키 값이 있는 5번째 컬럼(몸무게)를 float로 변환 시도
            line[5] = 0.0  # 나중에 BMI값을 계산하여 넣을 컬럼, 0으로 초기화
            table.append(line) # 변환된 데이터를 table에 추가
        except ValueError: # 변환할 수 없는 값이 있어 오류 처리
            continue  # 변환할 수 없는 값이 있으면 해당 행은 건너뜀
    f.close() # 파일을 닫음
random.shuffle(table) # 파일을 임의로 섞음


# 두 개의 입력값 받아 들이기
n = int(input("데이터 개수:") )  # 데이터 개수를 입력 받음
cmd = int(input("알고리즘 유형:")) # 알고리즘 유형 1 : O(n^2) 알고리즘, 2 : O(n) 알고리즘
table = table[:n]
startTime = time.time() # 측정 시작
##################################################################
# TO DO : 이 지점부터 수강생의 코딩을 시작함
# 학번 : 202210587 
# 이름 : 정선연

"""
line[3] = 키mm, line[4] = 몸무게kg, line[5] = BMI
"""
def compute_bmi_inplace(table):
    for row in table:
        try:
            height_mm = float(row[3]) / 1000.0
            weight_kg = float(row[4])
            row[5] = 0.0 if height_mm <= 0 else (weight_kg / (height_mm * height_mm))
        except Exception:
            row[5] = 0.0

"""
O(n^2) 삽입정렬 : line[5] BMI ASC정렬
원본리스트 : in-place
"""
def insertion_sort_by_bmi(arr):

    nlen = len(arr)
    for i in range(1, nlen):
        cur = arr[i]
        j = i - 1
        # cur의 BMI보다 큰 값들을 한 칸 뒤로 미룸
        while j >= 0 and float(arr[j][5]) > float(cur[5]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur

"""
평균 O(n) 버킷정렬 : BMI 범위를 K개 버킷으로 균등분할 -> 각 버킷 내부는 삽입정렬로 정렬
return : 정렬된 new list
"""
def bucket_sort_by_bmi(arr):
    nlen = len(arr)
    if nlen == 0:
        return []

    # BMI 최소/최대 탐색
    minv = float(arr[0][5])
    maxv = float(arr[0][5])
    
    for row in arr:
        v = float(row[5])
        if v < minv: minv = v
        if v > maxv: maxv = v

    if maxv == minv:
        return arr[:]  # 모든 BMI동일

    # 버킷 개수 : sqrt(n) 사용 -> 최소 10개
    k = int(nlen ** 0.5)
    if k < 10:
        k = 10

    buckets = [[] for _ in range(k)]

    # 각 원소 버킷에 분배
    rng = maxv - minv
    for row in arr:
        v = float(row[5])
        idx = int((v - minv) / rng * (k - 1))
        buckets[idx].append(row)

    # 각 버킷 내부는 삽입정렬 후 연결
    result = []
    for b in buckets:
        if b:
            insertion_sort_by_bmi(b)  # in-place
            for item in b:  # 이어붙이기
                result.append(item)

    return result

"""
(1) BMI 계산
"""
compute_bmi_inplace(table)

"""
(2) 알고리즘 수행
"""
if cmd == 1:
    # 삽입정렬
    insertion_sort_by_bmi(table)
elif cmd ==2:
    # 버킷정렬
    table = bucket_sort_by_bmi(table)
else:
    print("알고리즘 유형은 1 또는 2 중 하나여야합니다.")

###################################################################
# table 에 최종 정렬된 데이터가 저장되어 있다고 가정함

index = n//2 # 중위값 인덱스 계산
line = table[index] # 중위값 행을 끄집어 냄
if(n % 2 == 1) : # 데이터 개수가 홀수 이면
    median = line[5] # 가운데 값을 중위값으로 지정
else :              # 데이터 개수가 짝수 이면
    line2 = table[index-1] # 가운데 값이 두 개이므로 두 개를 모두 끄집어 냄
    median = (line[5] + line2[5]) /2  # 두 값의 평균을 중위값으로 지정

endTime = time.time() # 측정 종료
print("중위값:" + str(round(median,5)))  # 중위값 출력
print("수행시간:" + str(endTime - startTime)) # 정렬 수행 시간 출력

# write output file
f = open("prob2-result.csv",'w',newline='') # 출력 파일 오픈
wdr = csv.writer(f) # 파일 포인터 생성
wdr.writerows(table) # 결과 table을 csv 파일로 쓰기
f.close()  # 파일 닫음