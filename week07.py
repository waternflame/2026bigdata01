# 3) 넘파이 배열 연산
import numpy as np #numpy는 파이썬에서 수치 계산을 빠르게 도와주는 라이브러리
import random #random 모듈을 import 해옴
#l1 = [9, '짬뽕', 3.7, [1, 2, 3]] # 정수, 문자열, 실수, 리스트
#l1 = [9, '짬뽕', 3.7] # 정수, 문자열, 실수
#array01 = np.array(l1)
#print(l1)
#print(array01)
#
array02 = np.arange(10) #arange(10)은 0부터 9까지 10개의 원소를 가진걸 뜻함
print(array02)
#
#array03 = np.ones((2, 4)) #2행 4열이 출력됨
#array03 = np.ones((2, 4), dtype=int) #데이터 타입을 int로 바꿔서 출력
#print(array03)
#print(array03.T) #2행 4열이 4행 2열로 돌아가서 출력됨, 전치행렬
#전치행렬은 행렬의 행과 열을 서로 바꾼 행렬을 의미함

#array04 = np.random.rand() #0에서 1사이의 실수값이 하나 나옴
#array04 = np.random.rand(2, 3)
#print(array04)
#print(array04.transpose()) #transpose()는 .T와 같음

l2 = list()

l3 = []
for i in range(3):
    l2.append(random.random())
print(l2)

for item in l2:
    l3.append(item * 10)
print(l3)

array04 = np.array(l2)
print(array04 * 10)
#print(array04 > 5) # 실행 결과 false false false
print(array04 > 0.5) # 실행 결과 false false true

# 4) 넘파이 배열 주요 통계함수
print(np.mean(array02)) # 0부터 9를 가진 배열의 통계 출력됨
print(np.median(array02)) # 배열의 중앙값 출력됨
print(np.max(array02)) # 배열의 값 중 가장 큰 수를 출력
print(np.min(array02)) # 배열의 값 중 가장 작은 수를 출력
print(np.var(array02))
print(np.std(array02)) # 배열의 표준편차 값을 출력