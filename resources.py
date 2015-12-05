from models import Gene
from db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

gene_fields = {
    'id': fields.Integer,
    'symbol': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('symbol', type = str)

class GeneResource(Resource):
    @marshal_with(gene_fields)
    def get(self, id):
        gene = session.query(Gene).filter(Gene.id == id).first()
        if not gene:
            abort(404, message="Gene {} does not exist".format(id))

        return gene

class GeneListResource(Resource):
    @marshal_with(gene_fields)
    def post(self):
        parsed_args = parser.parse_args()
        gene = Gene(symbol = parsed_args['symbol'])
        session.add(gene)
        session.commit()

        return gene, 201
