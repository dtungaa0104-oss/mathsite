from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/engagement')
def engagement():
    return render_template('engagement.html')

@app.route('/learning')
def learning():
    return render_template('learning.html')

@app.route('/apps')
def apps():
    return render_template('apps.html')

@app.route('/local')
def local():
    return render_template('local.html')

if __name__ == '__main__':
    app.run(debug=True)
