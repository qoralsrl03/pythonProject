print("hi")
#글씨 보이나요?
#문자열은 '' or "" 긴문자열 쓸경우 ''' ''', ""' """
# a = "hi"
#print(a*100)
#print(type(a)) #type 함수는 자료의 타입을 볼때 사용
#a=1
#print(type(a))
#a = str(a) # to str
#print(type(a))
#a = int(a) # to int
#print(type(a))

#동적 배열
arr = [] #빈 배열
arr.append(1)
arr.append('hi')
arr.append([1,2,3,4])
# print(arr)
# print(arr[2])
# print(arr[2][3])
# print('슬라이스 1:3 ->', arr[0:1]) # 0의 자리부터 1의 자리를 미포함한 자리
# print(arr*100)

print('-'*100)
#반복문 for (3가지)
for i in (1,10):
    print(i)

# 1. 값만 필요할 떄
for v in arr:
    print(v) #<-- v는 순차적인 배열의 값
# 2. 인덱스값과 밸류값이 필요할때
for i, v in enumerate(arr):
    print('idx:', i, 'val:', v)

# 3. 단순 반복이 필요할때
for i in range(1,11):
    print(i)
# for i in range(len(arr)): #len -> length 배열의 길이만 큼반복
#     print(arr[i])

msg = input('숫자를 입력해 주세요 ^^:')
#input의 입력값은 문자열
for i in range(int(msg)):
    print(i)