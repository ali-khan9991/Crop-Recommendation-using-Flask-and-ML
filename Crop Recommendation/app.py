from flask import Flask,request,render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('login.html')

database = {'hayak':'salma','ikrus':'ronin'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('login.html',info='invalid username')
    else:
        if database[name1] != pwd:
            return render_template('login.html',info='invalid password')
        else:
            return render_template('index.html',name=name1)

@app.route('/predict',methods=['POST',"GET"])
def predict():
    int_features=[int(float(x)) for x in request.form.values()]
 
    final = [np.array(list(int_features))]
    print(final)
    prediction = model.predict(final)
    return render_template('index.html',pred='The Recommended crop is {}'.format(prediction[0]))


if __name__ ==  '__main__':
    app.run(debug=True)