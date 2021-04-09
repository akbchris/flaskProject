import json

from flask import Flask, request, jsonify
import object_detection
app = Flask(__name__)


@app.route('/api/detectImage', methods=["POST"])
def detectImage():
    record = json.loads(request.data)
    objectId = record['url']
    res = object_detection.detectImage(objectId)
    """

    :rtype: json
    """
    return json.dumps(res), 200


if __name__ == '__main__':
    app.run()
