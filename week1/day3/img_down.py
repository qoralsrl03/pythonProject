from urllib import request
import os
img_dir='./images'
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

url='https://image.fmkorea.com/files/attach/new2/20220819/494354581/2793993530/4937877951/b1efe5817fc4c5a39dc5447986342330.png'
request.urlretrieve(url, img_dir+'test.jpg')
