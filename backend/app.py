from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app, origins=['http://fahmed.pythonanywhere.com', 'http://localhost:3000'])

config = {
  'user': 'fahmed',
  'password': 'scribble123',
  'host': 'fahmed.mysql.pythonanywhere-services.com',
  'port': '3306',
  'database': 'fahmed$banglalearning'
}

def execute_query(query, params=None, fetch=True, fetchone=False, fetchall=False):
  try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute(query, params)

    if fetch:
      if fetchone:
        result = cursor.fetchone()
      else:
        result = cursor.fetchall()
    else:
      connection.commit()
      result = None

    cursor.close()
    connection.close()

    return result
  except Exception as e:
    return str(e)


@app.route('/')
def home():
  return jsonify({
    'message': 'Hi hi hiii'
  })

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')