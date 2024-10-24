from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/textinput")
def text():
    return render_template('textinput.html')

@app.route('/imageinput')
def image():
    return render_template('imageinput.html')

if __name__ == '__main__':
    app.run(debug=True)