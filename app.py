from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

from resources import GeneResource, GeneListResource

api.add_resource(GeneResource, '/genes/<string:id>', endpoint = 'gene')
api.add_resource(GeneListResource, '/genes', endpoint = 'genes')

if __name__ == '__main__':
    app.run(debug = True)
