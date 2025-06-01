from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello Prerna, I deployed this flask-app successfully on Render!")

if __name__ == '__main__':
    app.run(debug=True)
