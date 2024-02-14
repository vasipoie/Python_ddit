from flask import Flask,request,redirect,jsonify
from flask.templating import render_template
from day13.daoemp import DaoEmp


app = Flask(__name__)

@app.route('/')
def root():
    return redirect("static/emp.html")

@app.route('/ajax', methods=['POST'])
def ajax():
    menu = request.form["menu"]
    print(menu)
    return jsonify(result = menu)


@app.route('/emp_list', methods=['POST'])
def emp_list():
    de = DaoEmp()
    list = de.select()
    return jsonify(list = list)


@app.route('/emp_one', methods=['POST'])
def emp_one():
    e_id = request.form["e_id"]
    de = DaoEmp()
    vo = de.selectOne(e_id)    
    return jsonify(vo = vo)

@app.route('/emp_add', methods=['POST'])
def emp_add():
    e_id = request.form["e_id"]
    e_name = request.form["e_name"]
    gen = request.form["gen"]
    addr = request.form["addr"]
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    
    return jsonify(cnt = cnt)

@app.route('/emp_mod', methods=['POST'])
def emp_mod():
    e_id = request.form["e_id"]
    e_name = request.form["e_name"]
    gen = request.form["gen"]
    addr = request.form["addr"]
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    
    return jsonify(cnt = cnt)

@app.route('/emp_del', methods=['POST'])
def emp_del():
    e_id = request.form["e_id"]
    
    de = DaoEmp()
    cnt = de.delete(e_id)
    
    return jsonify(cnt = cnt)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
