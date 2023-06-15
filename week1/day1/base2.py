# set 중복없이 유니크한 값만 얻고자 할때
my_set = {1,2,3,4,5}
print(my_set)
my2_set = set()
print(type(my2_set))
my2_set.add(99)
my2_set.add(1) #하나만 추가 --> .add 를 사용하면 set에 순차적으로 세팅되는것이 아닌 넣은 순서대로 들어감

# my2_set.update({4,2,11,10,6}) #여러개 추가, 단 넣은 순서대로 출력되는것이 아닌 2,3, 6,10, 11 순차적으로 출력됨
print(my2_set)
print('---------')

#교집합
a= my_set&my2_set
print(a)
#합집합
b=my_set|my2_set
print(b)
#차집합
c=my_set - my2_set
print(c)