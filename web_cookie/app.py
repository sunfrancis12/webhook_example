from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('test.html')

@app.route('/cookie', methods=['GET'])
def cookie():
    return render_template('webhook.html')

@app.route('/steal', methods=['GET'])
def steal():
    return render_template('steal.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)