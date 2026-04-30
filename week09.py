import pandas as pd

df = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9], '화':[10, 3, 11]}, index=[1, 2, 3])
print(df)
print(df.iat[1, 2]) #정확한 좌표값을 추출
print(df.at[2, '수']) #라벨 기준
print(df.sample(frac=0.33)) #frac으로 준 퍼센트 만큼 값 추출, 여기선 3개 중에 1개를 추출함
print(df.nlargest(2, columns='화')) #가장 점수가 높은 2명을 추출, n=인원수
print(df.nsmallest(2, columns='화')) #가장 점수가 낮은 2명을 추출
print(df.tail(2)) #값에 대해서 상관없이 밑에서 2명 추출