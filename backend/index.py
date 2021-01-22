from flask import Flask, jsonify, Response, request
app = Flask(__name__)
    
@app.route('/', methods=['GET'])
def getme():
    return str('Backend is live')
    

@app.route('/api', methods=['GET', 'POST'])
def api():
    method = ""
    if request.method == "POST":
        method = "Post"
    else:
        method = "Get"
    return jsonify({"method": method})
