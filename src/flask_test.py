# -*- coding: utf-8 -*-
'''
@author: Pablo
'''
import json

import bson
from bson import json_util
import flask
import flask_pymongo
import flask_restful
from webargs import fields, flaskparser


APP_DEBUG_MODE = False
APP_URL = "http://127.0.0.1:5000"


def jsonifyBson(*args, **kwargs):
    '''
    This is needed because flask.jsonify can't serialize bson.ObjectId objects.

    Important! Allways use flask.jsonify due security reasons:
    http://flask.pocoo.org/docs/0.10/security/#json-security
    '''
    dumped = json_util.dumps(*args, **kwargs)
    loaded = json.loads(dumped)
    return flask.jsonify(loaded)


class Loan(flask_restful.Resource):
    '''
    It manage individual loan requests.

    Allowed HTTP methods:
        DELETE
        GET
        PATCH
        POST
    '''
    loan_args = {
      "age": fields.Integer(required=True),
      "income": fields.Float(required=True),
      "employed": fields.Boolean(required=True)
    }

    id_args = {
      "id": fields.String(required=True,
                          validate=bson.objectid.ObjectId.is_valid),
    }

    mongo = None

    def get(self, loan_id):
        if not bson.objectid.ObjectId.is_valid(loan_id):
            return jsonifyBson({"message": "Invalid loan id."}), 422  # Unprocessable Entity
        data = Loan.mongo.db.loan.find_one_or_404({"_id": bson.objectid.ObjectId(loan_id)})
        return jsonifyBson(data)

    @flaskparser.use_args(loan_args)
    def patch(self, args, loan_id):
        if not bson.objectid.ObjectId.is_valid(loan_id):
            return jsonifyBson({"message": "Invalid loan id."}), 422  # Unprocessable Entity
        Loan.mongo.db.loan.update_one({"_id": bson.objectid.ObjectId(loan_id)},
                                 {'$set': args})
        return flask.redirect(flask.url_for("loans_list"))

    def delete(self, loan_id):
        if not bson.objectid.ObjectId.is_valid(loan_id):
            return {"message": "Invalid loan id."}, 422  # Unprocessable Entity
        Loan.mongo.db.loan.remove({"_id": bson.objectid.ObjectId(loan_id)})
        return flask.redirect(flask.url_for("loans_list"))

    @flaskparser.use_args(loan_args)
    def post(self, args, loan_id=None):
        if loan_id:
            data = {"message": "The method is not allowed for the requested URL."}
            return data, 405  # METHOD NOT ALLOWED
#         data = flask.request.get_json()
        inserted_id = Loan.mongo.db.loan.insert_one(args)
        args.update({'id': str(inserted_id.inserted_id)})
        return jsonifyBson(args)


class LoanList(flask_restful.Resource):
    '''
    It manage loans list requests.
 
    Allowed HTTP methods:
        GET
    '''
    mongo = None

    def get(self):
        cursor = LoanList.mongo.db.loan.find({}).limit(10)
        data = [loan for loan in cursor]
        return jsonifyBson(data)


def create_mongo(app):
    return flask_pymongo.PyMongo(app, config_prefix='MONGO')


def update_mongo_instance(app):
    nongo = create_mongo(app)
    Loan.mongo = nongo
    LoanList.mongo = nongo


def create_and_run_flask_app(db_name):
    app = flask.Flask(__name__)
    app.config["MONGO_DBNAME"] = db_name
    update_mongo_instance(app)
    api = flask_restful.Api(app)
    api.add_resource(LoanList, "/", endpoint="loans_list")
    api.add_resource(Loan,
                     "/application",
                     "/application/<string:loan_id>",
                     endpoint="loan")

    @app.errorhandler(422)
    def handle_unprocessable_entity(err):
        # webargs attaches additional metadata to the `data` attribute
        exc = getattr(err, 'exc')
        if exc:
            # Get validations from the ValidationError object
            messages = exc.messages
        else:
            messages = ['Invalid request']
        return jsonifyBson({
            'messages': messages,
        }), 422

    app.run(debug=APP_DEBUG_MODE)


if __name__ == '__main__':
    import argparse

    def get_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--dbname",
                            help="Name of the MongoDB of the application.")
        return parser.parse_args()

    args = get_arguments()
    db_name = args.dbname if (args.dbname) else 'loans_db'

    create_and_run_flask_app(db_name)

