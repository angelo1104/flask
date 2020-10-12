from flask import Flask , request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/model',methods=['POST','GET'])
def model():
    if request.method == 'POST':
        return request.get_json()
    

if __name__ == '__main__':
    app.run()