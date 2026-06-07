import threading
import time
import requests
import os
from datetime import datetime

# Background keep-alive thread
def keep_render_awake():
    """Pings the site every 5 minutes to prevent Render sleep"""
    while True:
        try:
            if os.environ.get('RENDER'):
                url = f"https://{os.environ.get('RENDER_SERVICE_NAME', 'anmolsrw')}.onrender.com"
                response = requests.get(url, timeout=10)
                print(f"[{datetime.now()}] ✅ Pinged {url} - Status: {response.status_code}")
        except Exception as e:
            print(f"[{datetime.now()}] ⚠️ Keep-alive ping failed: {str(e)[:50]}...")
        time.sleep(300)

if os.environ.get('RENDER'):
    print("🚀 Starting keep-alive thread for Render...")
    keep_alive_thread = threading.Thread(target=keep_render_awake, daemon=True)
    keep_alive_thread.start()

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

# Individual class pages (keep old URLs working too)
@app.route('/class12')
def class12():
    return render_template('class12.html')

@app.route('/class11')
def class11():
    return render_template('class11.html')

@app.route('/class10')
def class10():
    return render_template('class10.html')

# Robotics & IoT
@app.route('/iot')
def iot():
    return render_template('iot.html')

# New pages
@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
