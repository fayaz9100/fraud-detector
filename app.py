from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['GET', 'POST'])
def result():

    if request.method == 'GET':
        return "Please submit the form to see prediction."

    features = np.array([
        float(request.form['step']),
        float(request.form['type']),
        float(request.form['amount']),
        float(request.form['oldbalanceOrg']),
        float(request.form['newbalanceOrig']),
        float(request.form['oldbalanceDest']),
        float(request.form['newbalanceDest']),
        float(request.form['isFlaggedFraud'])
    ]).reshape(1, -1)

    score = model.decision_function(features)[0]
    risk = round((score + 1) * 50, 2)

    if risk > 60:
        prediction = "🚨 Fraudulent Transaction"
        color = "danger"
    else:
        prediction = "✅ Legitimate Transaction"
        color = "success"

    return render_template(
        'result.html',
        prediction=prediction,
        risk=risk,
        color=color
    )

if __name__ == "__main__":
    app.run(debug=True)
