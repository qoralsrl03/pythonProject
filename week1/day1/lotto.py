import random


arr=[]

msg=int(input('몇개 생성할까요?:'))
for v in range(msg):
    com_set = set()
    while True:
        # com=[]
        # com.append()
        com_set.add(random.randint(1,45))
        if len(com_set)==6:
            arr.append(com_set)
            break;
print('-'*100)
for i in range(msg):
    print(arr[i])


