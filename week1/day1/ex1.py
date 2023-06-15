import random #라이브러리 임포트
com = random.randint(1,10) # 1~10 랜덤값
print(com)
while True:
    msg = int(input('숫자 맞추기!! 1~10 값을 입력하세요:'))
    # 조건문
    if com == msg:
        print('맞았음 !!')
        break
    else:
        print('틀렸음')
        if com > msg:
            print('힌트:', 'up')
        elif msg>10:
            print('10 이하로 입력하세요 !!!')
        else:
            print('힌트:','down')

arr = [1, 'hi']
print(arr)

for i in range(100):
    print(arr)

arr.append('bye')
for v in range(100):
    print(arr)