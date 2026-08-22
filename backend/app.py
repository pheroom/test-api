from flask import Flask, jsonify
import psycopg2
from os import getenv

app = Flask(__name__)

def get_db():
    conn = psycopg2.connect(getenv('DATABASE_URL'))
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Server is running! ver. 2", "status": "ok"})

@app.route('/api/health')
def health():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        conn.close()
        return jsonify({"database": "connected"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
