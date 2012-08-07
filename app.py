from flask import Flask, request
import pprint, json, os

app = Flask(__name__)

@app.route('/gitty/', methods=["POST"])
def root():
    if 'payload' in request.form.keys():
        obj = json.loads(request.form['payload'])
        if obj['ref'] == 'refs/head/deploy':
        	os.popen('git pull origin deploy')
    return ":3"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
