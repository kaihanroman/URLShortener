from flask import Flask, redirect, render_template, request
import json
import random
import string
app = Flask(__name__)

def generateHash():
    # Takes random choices from
    # ascii_letters and digits
    newHash = ''.join([random.choice(
                        string.ascii_letters + string.digits)
                        for n in range(7)])

    return newHash
@app.route("/")
def index():
    return render_template('layout.html')

@app.route("/check/", methods=['GET'])
def checkStatus():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route("/go/<string:key>", methods=['GET'])
def goToUrl(key):
    with open('storage.json', 'r+') as f:
        data= json.load(f)
        url = data[key]
        return redirect(url, code=302)

@app.route("/addUrl/", methods=['POST'])
def addUrl():
    key = generateHash()
    obj = request.get_json()
    print(obj)
    oldUrl = obj['oldUrl']
    with open('storage.json', 'r+') as f:
        data = json.load(f)
        while(data.has_key(key)):
            key = generateHash();
        data[key] = oldUrl
    with open('storage.json', 'w+') as f:
        json.dump(data, f)
    newUrl = "go/" + key
    obj['newUrl'] = newUrl
    obj = json.dumps(obj)
    return obj



if __name__ == "__main__":
    app.run()



