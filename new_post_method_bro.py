
from flask import Flask ,request
from flask_restful import Resource, Api 

app = Flask(__name__) # here we are creating Flask app
api = Api(app) # here we creating instance of Flask

class First(Resource):
    def get(self):
        return {"status": "success", "msg": "api created"}, 200
    def post(self):
         body = request.get_json()
         return {"status":"success",'result' :body["a"] + body["b"]},201
        
api.add_resource(First, "/dev/v1/api/status")

if __name__ == "__main__":
    app.run(host="192.168.55.102", port=8055)