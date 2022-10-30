from re import T
from flask import Flask, render_template, request
import app as model


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def display():
 if request.method == 'POST':
  model.main()
 return render_template('index.html')


if __name__ == '__main__':
 app.run(debug=True)



