from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/class12')
def class12():
    return render_template('class12.html')

@app.route('/class11')
def class11():
    return render_template('class11.html')

@app.route('/iot')
def iot():
    return render_template('iot.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)  # debug=False for production