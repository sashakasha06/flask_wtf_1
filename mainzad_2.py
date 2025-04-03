from flask import Flask, render_template, json

app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/training/<profession>')
def index(profession):
    print(profession)
    return render_template('shablon_2.html', prof=profession)

if __name__ == '__main__':
    app.run(port=4019, host='127.0.0.1')