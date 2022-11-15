from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def details():
    return render_template('index.html')

@app.route("/techpoint")
def techpoint():
    return render_template('techpoint.html')

if __name__ == '__main__':
    app.run(debug=True)