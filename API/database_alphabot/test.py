from flask import Flask,url_for,jsonify,request,render_template
import utility_database_percorsi as db
        
app= Flask(__name__)
app.config["DEBUG"]= True

@app.route('/', methods=['GET'])
def home():
    return 'home'

@app.route('/api',methods=['GET'])
def api_all():
    return jsonify(db.read_all())

@app.route('/api/v1/resources/percorsi', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    return jsonify(db.search_by_id(id))

@app.route('/api/v1/resources/place', methods=['GET'])
def api_place():
    if 'place' in request.args:
        place = request.args['place']
    else:
        return "Error: No palce field provided. Please specify an place."
    return jsonify(db.search_by_place(place))

@app.route('/api/v1/resources/route', methods=['GET'])
def api_route():
    if 'start' in request.args and 'end' in request.args:
        start = request.args['start']
        end = request.args['end']
    else:
        return "Error: Start or End not specified. Please specify."
    return jsonify(db.search_route(start,end))

app.run()