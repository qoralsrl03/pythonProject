import os
print(os.getcwd()) # 현재 경로
path = os.getcwd() + "/files"
file_list = os.listdir(path) # 경로에 파일에 접근
for file_nm in file_list:
    #파일이 존재하면 true
    file_path = path + "/" + file_nm
    if os.path.exists(path + "/" + file_nm):
        print(file_nm)
        if os.path.isdir(file_path):
            print('디렉토리')
            os.rmdir(file_path) #폴더 삭제
        if os.path.isfile(file_path):
            print('파일임')
            os.remove(file_path) #파일 삭제


import os

path = os.getcwd() + "/files"

# 경로에 있는 파일 목록을 가져옵니다.
file_list = os.listdir(path)

for file_nm in file_list:
    # 파일 또는 디렉토리의 실제 경로를 생성합니다.
    file_path = os.path.join(path, file_nm)

    if os.path.exists(file_path):
        print(file_nm)
        if os.path.isdir(file_path):
            print('디렉토리')
            os.rmdir(file_path)  # 폴더 삭제
        if os.path.isfile(file_path):
            print('파일임')
            os.remove(file_path)  # 파일 삭제