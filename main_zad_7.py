from flask import Flask, render_template, json

app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/table/<sex>/<age>')
def index(sex, age):
    age = int(age)
    if sex == 'female' and age < 21:
        color = 'FFCCCB'
    elif sex == 'female' and age >= 21:
        color = 'FF0000'
    elif sex == 'male' and age < 21:
        color = 'ADD8E6'
    else:
        color = '0000FF'
    return render_template('shablon_7_1.html', sex=sex, age=age, wall_color=color)

if __name__ == '__main__':
    app.run(port=4019, host='127.0.0.1')