from flask import Flask, render_template

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
    app.run(debug=True)