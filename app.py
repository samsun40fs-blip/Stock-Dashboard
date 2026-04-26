from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/data')
def data():
    try:
        with open('scan_results.json', 'r') as f:
            return jsonify(json.load(f))
    except:
        return jsonify({"stocks": [], "meta": {"fear_greed": 50, "total_found": 0, "last_update": "ยังไม่มีข้อมูล"}})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
