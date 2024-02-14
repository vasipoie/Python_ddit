from flask import Flask,render_template
from flask import request
from day11.daomem import DaoMem
 
app = Flask(__name__)
 
@app.route('/')
@app.route('/mem_list')
def mem():
    dm = DaoMem()
    list = dm.select()
    return render_template('mem_list.html', list=list)

@app.route('/mem_detail')
def memDetail():
    m_id = request.args.get('m_id',"")
    dm = DaoMem()
    vo = dm.selectOne(m_id)
    return render_template('mem_detail.html', vo=vo)
    

@app.route('/mem_mod')
def memMod():
    m_id = request.args.get('m_id',"")
    dm = DaoMem()
    vo = dm.selectOne(m_id)
    return render_template('mem_mod.html', vo=vo)

@app.route('/mem_mod_act', methods=['POST'])
def memModAct():
    m_id = request.form["m_id"]
    m_name = request.form["m_name"]
    tel = request.form["tel"]
    email = request.form["email"]
    
    dm = DaoMem()
    cnt = dm.update(m_id, m_name, tel, email)
    return render_template('mem_mod_act.html', cnt=cnt)


@app.route('/mem_add')
def memAdd():
    return render_template('mem_add.html')

@app.route('/mem_add_act', methods=['POST'])
def memAddAct():
    m_id = request.form["m_id"]
    m_name = request.form["m_name"]
    tel = request.form["tel"]
    email = request.form["email"]
    
    dm = DaoMem()
    cnt = dm.insert(m_id, m_name, tel, email)
    return render_template('mem_add_act.html', cnt=cnt)


@app.route('/mem_del_act')
def memDelAct():
    m_id = request.args.get('m_id',"")
    dm = DaoMem()
    cnt = dm.delete(m_id)
    return render_template('mem_del_act.html', cnt=cnt)


if __name__ == '__main__':
    app.run(debug = True)
    