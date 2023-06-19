import requests
url = 'http://127.0.0.1:5000/todos'
#res = requests.post(url, data={"data":"study"})
res = requests.get(url + '/1')
#print(res)
res2 = requests.get(url+'/1')
print(res2)
print(res2.json())
res3 = requests.put(url+'/1',data={"data":"eat"})
print(res3)
print(res3.json())
res4 = requests.delete(url+'/1')
print(res4)
print(res4.json())