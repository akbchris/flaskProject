import json

from flask import Flask, request, jsonify
import object_detection

app = Flask(__name__)


@app.route('/api/detectImage', methods=["POST"])
def detectImage():
    record = json.loads(request.json)
    objectId = record['id']
    imageUrl = record['image']
    res = {
        "id": objectId,
        "objects": object_detection.detectImage(imageUrl)
    }
    """

    :rtype: json
    """
    return json.dumps(res), 200


if __name__ == '__main__':
    app.run(debug=True)
