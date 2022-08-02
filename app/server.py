from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong', 200

@app.route('/', methods=['GET', 'POST'])
def index():
   return 200 

@app.route('/classify', methods=['GET', 'POST'])
def get_class():
    """
    curl -d '{"text":"post message"}' -H "Content-Type: application/json" -X POST 127.0.0.1:5000/classify
    """
    if request.method=='GET':
        text = request.args.get('text')
    else:
        data = request.get_json()
        text = data['text']
    return jsonify({'answer':text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
