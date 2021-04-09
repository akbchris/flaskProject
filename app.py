import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/detectImage', methods=["POST"])
def detectImage():
    record = json.loads(request.data)
    objectId = record['id']
    """

    :rtype: json
    """
    return json.dumps({'id': '1111', }), 200


if __name__ == '__main__':
    app.run()
