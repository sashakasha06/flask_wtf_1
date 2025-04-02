from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
@app.route('/index/<title_name>')
def index(title_name):
    return render_template('shablon_1.html', title=title_name)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')