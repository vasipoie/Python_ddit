from flask import Flask,request,redirect,jsonify
from flask.templating import render_template
from day13.daoemp import DaoEmp


app = Flask(__name__)

@app.route('/')
def root():
    return redirect("static/ajax.html")

@app.route('/ajax1', methods=['POST'])
def ajax1():
    return jsonify(result = '2')

@app.route('/ajax2', methods=['POST'])
def ajax2():
    return jsonify(result = '20')


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
