from flask import Flask,render_template
from flask import request
from day09 import daoemp
from day09.daoemp import DaoEmp
 
app = Flask(__name__)
 
@app.route('/')
def hello_flask():
    return 'Hello Flask!'

@app.route('/param')
def param():
    menu = request.args.get('menu', "탕수육")
    return 'menu = '+menu

@app.route('/post', methods=['POST'])
def post():
    menu = request.form["menu"]
    return 'post : '+menu

@app.route('/forw')
def forw():
    a = "홍길동"
    b = ["바보","천재"]
    c = [
        {'e_id' : '1', 'e_name' : '1', 'gen' : '1','addr' : '1'}
        ,{'e_id' : '2', 'e_name' : '2', 'gen' : '2','addr' : '2'}
        ,{'e_id' : '3', 'e_name' : '3', 'gen' : '3','addr' : '3'}
        
        ]
    return render_template('forw.html', a=a, b=b, c=c)

@app.route('/emp')
def emp():
    de = DaoEmp()
    list = de.select()
    return render_template('emp.html', list=list)
 
if __name__ == '__main__':
    app.run(debug = True)
    