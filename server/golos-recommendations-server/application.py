from flask import Flask, jsonify, request, render_template
from config import config
import model.recommendations as recommendations_model
import json

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

@app.route('/recommendations')
def recommendations():
  user = float(request.args.get("user"))
  return jsonify(json.loads(recommendations_model.recommendations(user).to_json(orient='records')))

@app.route('/history')
def history():
  user = float(request.args.get("user"))
  return jsonify(json.loads(recommendations_model.history(user)[["title", "permlink", "parent_permlink", "topic", "like"]].to_json(orient='records')))

@app.route('/users')
def users():
  return jsonify(json.loads(recommendations_model.users().to_json(orient='records')))

if __name__ == '__main__':
  config(app)
  app.run(port=8080)
