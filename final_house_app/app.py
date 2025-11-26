from flask import Flask, request, jsonify, render_template
import json, pickle, numpy as np

app = Flask(__name__)

with open("C:\\Users\\prasa\\Desktop\\machine learning\\columns.json") as f:
    __data_columns = json.load(f)['data_columns']
    __locations = __data_columns[3:]

with open("c:\\Users\\prasa\\Desktop\\machine learning\\banglore_home_prices_model.pickle",'rb') as f:
    __model = pickle.load(f)

def get_estimated_price(location, sqft, bath, bhk):
    try: loc_index=__data_columns.index(location.lower())
    except: loc_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft; x[1]=bath; x[2]=bhk
    if loc_index>=0: x[loc_index]=1
    return round(__model.predict([x])[0],2)

@app.route('/')
def home():
    return render_template('index.html', locations=sorted(__locations))

@app.route('/predict', methods=['POST'])
def predict():
    d=request.form
    price=get_estimated_price(d['location'], float(d['area']), int(d['bath']), int(d['bhk']))
    return jsonify({'price':price})

if __name__=='__main__':
    app.run(debug=True)