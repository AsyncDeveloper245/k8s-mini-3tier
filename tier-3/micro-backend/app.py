from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# connect to the MongoDB database
client = MongoClient("db-service.dev.svc.cluster.local",27017)
db = client["links_db"]
collection = db["links"]

@app.route('/', methods=['POST', 'GET'])
def store_link():
    if request.method == 'POST':
        data = request.get_json()
        link = data['link']

        # store the link in the MongoDB database
        link_id = collection.insert_one({'link': link}).inserted_id

        return {'status':"success", 'data':link_id} , 200
    elif request.method == 'GET':
        # retrieve all the links from the MongoDB database
        links = [link for link in collection.find({}, {'_id': False})]
        print(links)
        return jsonify(links) , 200

    else:
        return {'status':"error"} , 400
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
