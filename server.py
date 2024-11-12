from flask import Flask, request
import json

# start a flask server
app = Flask(__name__)


@app.route('/log', methods=['POST'])
def log():
    # accept post requests (only accept certain format?)
    if request.method == 'POST':
        data = request.get_json()
        print(data)

        # append data to a file
        with open('metrics.json', 'a') as f:
            f.write(json.dumps(data) + "\n")
            f.close()

        return {'status': 'success'}, 200
