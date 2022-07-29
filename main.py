from flask import Flask, render_template, request
import json
from predictor import predictSomething 
import datetime

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
   return render_template("index.html", utc_dt=datetime.datetime.utcnow())

@app.route('/predict', methods=['GET'])
def predict():
    args = request.args
    print(predictSomething(args["query"]))
    return json.dumps({"predictionResponse": predictSomething(args["query"])})

if __name__ == '__main__':
   app.run()
#    app.run(debug = True)

app.run(host='0.0.0.0', port=3000)