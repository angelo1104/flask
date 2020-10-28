from flask import Flask , request ,jsonify
import json
import pickle
import numpy as np
from flask_cors import CORS


from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)


app = Flask(__name__)

cors = CORS(app)

@app.route('/')
def home():
    return "Hello"


@app.route('/model',methods=['POST','GET'])
def model():
    model = pickle.load(open('diet.sav','rb'))
    myList = []


    if request.method == 'POST':

        response = request.get_json()
        print(response)
        
        glucose = response.get('glucose')
        myList.append(float(glucose))
        bloodPressure = response.get('bloodPressure')
        myList.append(float(bloodPressure))
        
        bmi = response.get('bmi')
        myList.append(float(bmi))
        age = response.get('age')
        myList.append(float(age))
        #jgjhj
        gotList = np.array(myList)
        gotListPoly = poly_reg.fit_transform(gotList.reshape(1,-1))


        predictedValues = model.predict(gotListPoly)

        print(predictedValues)
        
        data = {
            "value": str(predictedValues[0])
        }

        myList = []
        return jsonify(data)
    

if __name__ == '__main__':
    app.run()