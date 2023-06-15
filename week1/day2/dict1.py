# 키(key) - 값(value)
param = {} # 비어있는 dict
print(type(param))
param['nm'] = '팽수'
param['age'] = 10
print(param)
param2={"nm" :"팽수", "age":30}
print(param2)
for key in param2:
    print("key:",key,"val:",param2[key])

# 불변형(immutable), 가변형(mutable)
# python 에서 불변형 자료는 : 숫자, 문자열, 튜플 -- 한번 주소에 할당하면 값을 바꿀수 없어, 값을 변경하면 주소도 바뀜, 실제 메모리 상에서 변경되지않고 그 값을 유지함
#            가변형 자료는 : array, dict, set -- 동일한 주소에 여러 값으로 변경이 가능함
nm = '팽수'
print(id(nm))
nm='팽팽수'
print(id(nm))
arr=[1,2]
print(id(arr))
arr[0] = 3
print(id(arr))
