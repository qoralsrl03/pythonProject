
    # num의 수 만큼 lotoo번호를 생성하여 리턴하는 함수.
import random

def make_lotto(num):
    result = []  # 생성된 로또 번호들을 담을 리스트
    for i in range(num):  # 입력받은 숫자(num)만큼 반복합니다.
        make_num = set()  # 중복을 허용하지 않는 set을 생성합니다.
        while len(make_num) < 6:  # 6개의 숫자가 생성될 때까지 반복합니다.
            make_num.add(random.randint(1, 45))  # 1부터 45까지의 난수를 생성하여 set에 추가합니다.
        result.append(make_num)  # 생성된 로또 번호를 결과 리스트에 추가합니다.
    return result

# make_lotto 함수를 호출하여 5개의 로또 번호를 생성합니다.
lotto_numbers = make_lotto(5)
print(make_lotto())


#모듈 자체 실행시 true
if __name__ == '__main__':
    print('모듈 자체 실행')
    lotto_num = make_lotto(3)
    print(lotto_num)
else :
    print('import 했음.')
