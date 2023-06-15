# 가변길이 파라미터
# 함수의 입력 파라미터의 갯수를 미리 알수 없을때 0 ~ n개 파라미터를 받을수있음
def fn_total(*numbers):
    tot = 0
    for n in numbers:
        tot += n
    return tot
print(fn_total(2, 4, 5))
print(fn_total(2, 2))
print(fn_total())

def fn_sum_mul(choice, *args):
    if choice == 'sum':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *=i
    return result
print(fn_sum_mul('sum', 1, 2, 3, 4,))
print(fn_sum_mul('mul', 1, 2, 3, 4,))



def fn_total2(*numbers):
    tot = 0
    cnt = 0
    for n in numbers:
        tot += n
        cnt += 1
    return tot, cnt
a , b = fn_total2(1,2,3,4,5,6,7)
c = fn_total2(1,2,3,4,5,6,7)
print('합계:', a, '횟수:', b)