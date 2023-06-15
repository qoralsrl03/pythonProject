import os


def fn_search(filename, path='/'):
    print('찾았습니다.')
    path = input('탐색 경로 입력: ')
    filename = input('찾고자 하는 파일명 입력: ')

    dir = os.path.abspath(path)

    for dirpath, dirnames, filenames in os.walk(dir):
        for file in filenames:
            if filename in file:
                print(os.path.join(dirpath, file))
                break




fn_search()
