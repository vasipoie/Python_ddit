from flask import Flask,render_template,redirect
from flask import request
from day09 import daoemp
from day09.daoemp import DaoEmp
from flask.helpers import make_response
from flask.json import jsonify
 
app = Flask(__name__)
 
@app.route('/')
def root():
    return redirect("static/ajax.html")

@app.route('/ajax', methods=['POST','GET'])
def ajax():
    menu = request.form["menu"]
    print(menu)
    return jsonify({'result' : 'success'})
 
if __name__ == '__main__':
    app.run(debug = True)
    