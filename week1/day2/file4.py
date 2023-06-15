import os
#filename을 포함하고 있는 파일 찾기
path = '/'
filename = '백민기'
dir = os.path.abspath(path)

for dirpath, dirnames, filenames in os.walk(dir):
    for file in filenames:
        #contains
        if filename in file:
            print(dirpath, file)
            msg = input('찾는 파일이 맞나요?(y/n) : ')
            if msg=='y':
                break

