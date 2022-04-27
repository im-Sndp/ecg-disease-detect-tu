from flask import *
import pandas as pd
import numpy as np
import os
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pickle

app = Flask(__name__)

def calculate(filename):
    with open('csv_convert','rb') as f:
        cf = pickle.load(f)

    with open('model_pickle','rb') as f:
        mp = pickle.load(f)

    test = pd.read_csv(filename)
    test = test.T
    result = mp.predict([test.to_numpy()[0]])
    os.remove(filename)
    return result[0]

@app.route('/')
def upload():
    return render_template("index.html")

@app.route('/tool', methods =["GET", "POST"])
def tool():
    return render_template("tool.html")

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        name = request.form['name']
        height = request.form['height']
        weight = request.form['weight']
        # age = request.form['age']
        gender = request.form['gender']
        result  = calculate(f.filename)

        return render_template("success.html", name=name , height=height , weight=weight , gender=gender , result = result)

if __name__ == '__main__':
    app.run(debug = True)
    app = Flask(__name__)
