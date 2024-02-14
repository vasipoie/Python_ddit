from flask import Flask,render_template
from flask import request
from day15.lite_naver import LiteNaver
 
app = Flask(__name__)
 
# @app.route('/')
# @app.route('/emp_list')
# def emp():
#     de = LiteNaver()
#     list = de.select()
#     return render_template('emp_list.html', list=list)
#
# @app.route('/emp_detail')
# def empDetail():
#     e_id = request.args.get('e_id',"")
#     de = LiteNaver()
#     vo = de.selectOne(e_id)
#     return render_template('emp_detail.html', vo=vo)

# @app.route('/emp_mod')
# def empMod():
#     e_id = request.args.get('e_id',"")
#     de = LiteNaver()
#     vo = de.selectOne(e_id)
#     return render_template('emp_mod.html', vo=vo)
#
# @app.route('/emp_mod_act', methods=['POST'])
# def empModAct():
#     e_id = request.form["e_id"]
#     e_name = request.form["e_name"]
#     gen = request.form["gen"]
#     addr = request.form["addr"]
#
#     de = LiteNaver()
#     cnt = de.update(e_id, e_name, gen, addr)
#     return render_template('emp_mod_act.html', cnt=cnt)


@app.route('/emp_add')
def empAdd():
    return render_template('emp_add.html')

@app.route('/emp_add_act', methods=['POST'])
def empAddAct():
    title = request.form["title"]
    link = request.form["link"]
    description = request.form["description"]
    bloggername = request.form["bloggername"]
    bloggerlink = request.form["bloggerlink"]
    postdate = request.form["postdate"]
    
    de = LiteNaver()
    cnt = de.insert(title, link, description, bloggername, bloggerlink, postdate)
    return render_template('emp_add_act.html', cnt=cnt)


# @app.route('/emp_del_act')
# def empDelAct():
#     e_id = request.args.get('e_id',"")
#     de = LiteNaver()
#     cnt = de.delete(e_id)
#     return render_template('emp_del_act.html', cnt=cnt)


if __name__ == '__main__':
    app.run(debug = True)
    