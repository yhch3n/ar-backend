from flask import Flask, jsonify, request, abort
from db.database import db_session, init_db
from db.models import ArDataAnnotation
import logging
from json import dumps
from schemas import ArDataSchema
from http import HTTPStatus

init_db()
app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def show_all():
    return jsonify(ArDataAnnotation.query.all())

@app.route('/ardata/<int:roomId>')
def get_data_by_roomid(roomId):
    data = ArDataAnnotation.query.filter(ArDataAnnotation.roomId == str(roomId)).all()
    logging.debug(data)

    if data is None:
        return (jsonify("Room not found"), 404)

    ar_data_schema = ArDataSchema(many=True)
    try:
        res = ar_data_schema.dump(data)
        return jsonify(res), HTTPStatus.OK
    except Exception as e:
        abort(400, e)

@app.route('/push_data', methods = ['POST'])
def push_data():
    request_data = request.get_json()
    logging.debug(request_data)

    arData = ArDataAnnotation(
        roomId = request_data['roomId'],
        keyword = request_data['keyword'],
        modelMatrix = request_data['modelMatrix'],
        anchorPose = request_data['anchorPose'],
        hashcode = request_data['hashcode']
    )
    db_session.add(arData)
    db_session.commit()
    return jsonify('OK'), 200


if __name__ == '__main__':
    app.run(debug=True)
