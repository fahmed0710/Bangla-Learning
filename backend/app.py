from Flask import Flask, jsonify, send_from_directory
from flask_cors import flask_cors
import mysql.connector

app = Flask(__name__)
CORS(app, origins=['http://fahmed.pythonanywhere/com', 'http://localhost:3000'])

config = {
  'user': 'fahmed',
  'password': 'scribble123',
  'host': 'fahmed.mysql.pythonanywhere-services.com',
  'port': '3306',
  'database': 'fahmed$banglalearning'
}

@app.route('/')
def home():
  return jsonify({
    'message': 'hi hiii :)'
  })

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')