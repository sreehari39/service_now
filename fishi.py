
from flask import  Flask
from flask_restful import Resource,Api
app = Flask(__name__)
api = Api(app)

class Fiest(Resource):
    def post(self):
        return {'result':'okokoko','msg':'okokk'}
api.add_resource(Fiest,"/dev/v1/api/status")
if __name__ == '__main__':
    app.run(host="192.168.55.108", port=8055)