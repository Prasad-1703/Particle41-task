from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_time_and_ip():
    visitor_ip = request.remote_addr
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({
        "timestamp": current_time,
        "ip": visitor_ip
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
