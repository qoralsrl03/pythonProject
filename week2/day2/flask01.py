#pip install flask_cors
from flask import Flask, render_template, request
import requests
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app) #전체 허용

@app.route("/")
def index():
    return render_template('index.html',name="Nick")
@app.route("/main",methods=['GET','POST'])
def main():
    if request.method == 'POST':
        data = json.loads(request.get_data(), encoding='urf-8')
        print(data)
        res = requests.get('https://api.upbit.com/v1/ticker?market='+data['test'])
        return res.content
    else:
        print('get')
        res = requests.get("https://api.upbit.com/v1/market/all")
        coin_list = json.loads(res.content)
        return render_template('main.html',coins=coin_list)

if __name__ == '__main__':
    app.run(debug=True, port=5555)