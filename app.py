from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    # This proves we can talk to your Postgres DB
    db_host = os.getenv('DB_HOST', 'postgres-service')
    return f"""
    <body style="background-color: #0d1117; color: white; font-family: sans-serif; text-align: center; padding-top: 50px;">
        <h1>🚀 DevOps Project: Live Metrics</h1>
        <div style="border: 2px solid #238636; display: inline-block; padding: 20px; border-radius: 10px;">
            <p>Status: <span style="color: #238636;">Connected to Cluster</span></p>
            <p>Database: <span style="color: #58a6ff;">{db_host}</span></p>
        </div>
    </body>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
