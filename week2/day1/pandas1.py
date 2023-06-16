import pandas as pd

#pandas 의 기본 형태는 dataframe
df = pd.DataFrame({"name" : ["nick", "judy", "jack"]
                   ,"age" :[10,15,20]})

df['age_plus'] = df['age'] + 1
df['age_squared'] = df['age'] * df['age']
df['over_15'] = df['age'] > 15
print(df.head()) #내용 출력 기본 5행

print('=' * 100)
total = df['age'].sum() #특정 열의 각 행의 합
print(total)

print('=' * 100)
# 데이터 기본정보
print(df.info()) #df의 정보 요약

print('=' * 100)
# 데이터 기초통계량
print(df.describe())
# 함수 적용가능
df2 = df['age'].apply(lambda x : x * x)

print('=' * 100)
# join
df2 = pd.DataFrame({"name" : ["nick", "judy", "jack"]
                    ,"height" : [180, 165, 187]
                   , "gender" : ["M","F","M"]})
joined = df.set_index("name").join(df2.set_index("name")) #DB처럼 조인시키기
print(joined.head())

print('=' * 100)
# group by
print(joined.groupby('gender').mean())