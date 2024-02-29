from flask import Flask,request,redirect,jsonify
from flask.templating import render_template
from day13.daoemp import DaoEmp


app = Flask(__name__)

@app.route('/')
def root():
    return redirect("static/kakaomap2.html")



if __name__ == '__main__':
    app.run(debug=True)