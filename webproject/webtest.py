
from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__, template_folder='./src/templates',
            static_folder='./src/static')
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/index.html")
def index1():
    return render_template('index.html')

@app.route("/mesh.html")
def mesh():
    return render_template('mesh.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
