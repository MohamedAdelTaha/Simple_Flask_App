from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Hello World!'

@app.route('/storepage')
def store_page_test():
    return 'Hello From store web page!'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)