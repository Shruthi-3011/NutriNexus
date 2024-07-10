import numpy as np
from flask import Flask,request,render_template,redirect, url_for
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)
sc =pickle.load(open('sc.pkl','rb'))
model =pickle.load(open('classifier.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET','POST']) 
def signin():
    if request.method=='POST':
        float_features=[float(x) for x in request.form.values()]
        age=float(request.form.get('age'))
        if age <= 10:
            age_group = "0 to 10"
        elif age <= 30:
            age_group = "11 to 30"
        elif age <= 60:
            age_group = "31 to 60"
        else:
            age_group = "Above 60"
        final_features=[np.array(float_features)]
        pred= model.predict(sc.transform(final_features))[0]
        return render_template('result.html', prediction=pred,age_group=age_group, age=age)
    else:
        return render_template('signin.html')


@app.route('/breakfastonetoten')
def breakfastonetoten():
    return render_template('breakfastonetoten.html')

@app.route('/lunchonetoten')
def lunchonetoten():
    return render_template('lunchonetoten.html')

@app.route('/dinneronetoten')
def dinneronetoten():
    return render_template('dinneronetoten.html')

@app.route('/breakfasttothirty')
def breakfasttothirty():
    return render_template('breakfasttothirty.html')

@app.route('/lunchtothirty')
def lunchtothirty():
    return render_template('lunchtothirty.html')

@app.route('/dinnertothirty')
def dinnertothirty():
    return render_template('dinnertothirty.html')

@app.route('/breakfasttosixty')
def breakfasttosixty():
    return render_template('breakfasttosixty.html')

@app.route('/lunchtosixty')
def lunchtosixty():
    return render_template('lunchtosixty.html')

@app.route('/dinnertosixty')
def dinnertosixty():
    return render_template('dinnertosixty.html')

@app.route('/breakfastabovesixty')
def breakfastabovesixty():
    return render_template('breakfastabovesixty.html')

@app.route('/lunchabovesixty')
def lunchabovesixty():
    return render_template('lunchabovesixty.html')

@app.route('/dinnerabovesixty')
def dinnerabovesixty():
    return render_template('dinnerabovesixty.html')

@app.route('/ndbreakfastonetoten')
def ndbreakfastonetoten():
    return render_template('ndbreakfastonetoten.html')

@app.route('/ndlunchonetoten')
def ndlunchonetoten():
    return render_template('ndlunchonetoten.html')

@app.route('/nddinneronetoten')
def nddinneronetoten():
    return render_template('nddinneronetoten.html')

@app.route('/ndbreakfasttothirty')
def ndbreakfasttothirty():
    return render_template('ndbreakfasttothirty.html')

@app.route('/ndlunchtothirty')
def ndlunchonetothirty():
    return render_template('ndlunchtothirty.html')

@app.route('/nddinnertothirty')
def nddinnertothirty():
    return render_template('nddinnertothirty.html')

@app.route('/ndbreakfasttosixty')
def ndbreakfasttosixty():
    return render_template('ndbreakfasttosixty.html')

@app.route('/ndlunchtosixty')
def ndlunchtosixty():
    return render_template('ndlunchtosixty.html')

@app.route('/nddinnertosixty')
def nddinnertosixty():
    return render_template('nddinnertosixty.html')

@app.route('/ndbreakfastabovesixty')
def ndbreakfastabovesixty():
    return render_template('ndbreakfastabovesixty.html')

@app.route('/ndlunchabovesixty')
def ndlunchabovesixty():
    return render_template('ndlunchabovesixty.html')

@app.route('/nddinnerabovesixty')
def nddinnerabovesixty():
    return render_template('nddinnerabovesixty.html')


if __name__ == '__main__':
    app.run(debug=True)



