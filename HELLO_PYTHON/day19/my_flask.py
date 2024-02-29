from flask import Flask,request,redirect,jsonify
from flask.templating import render_template
from day13.daoemp import DaoEmp
from day19.daobline import DaoBLine


app = Flask(__name__)
dbl = DaoBLine()


@app.route('/')
def root():
    return redirect("static/kakaomap.html")

@app.route('/near5', methods=['POST'])
def near5():
    lat = request.form["lat"]
    lng = request.form["lng"]
    list = dbl.near5(lng, lat)
    return jsonify(list = list)

@app.route('/getbusids', methods=['POST'])
def getbusids():
    s_id = request.form["s_id"]
    list = dbl.getBusIdsBySid(s_id)
    return jsonify(list = list)

@app.route('/getpath', methods=['POST'])
def getpath():
    bus_id = request.form["bus_id"]
    list = dbl.getPathByBusId(bus_id)
    return jsonify(list = list)
    

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
