from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"message": "server is up and running"})

if __name__ == '__main__':
    app.run(debug=True)
