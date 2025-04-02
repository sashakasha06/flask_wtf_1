from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def show_form():
    return render_template('auto_answer.html', title='Anket')
@app.route('/submit', methods=['POST'])
def submit():
    user_data = {}
    user_data['Фамилия'] = request.form['surname']
    user_data['Имя'] = request.form['name']
    user_data['Образование'] = request.form['education']
    user_data['Профессия'] = request.form['profession']  # Опечатка здесь - должно быть 'profession'
    user_data['Пол'] = request.form['sex']
    user_data['Мотивация'] = request.form['motivation']
    user_data['Готовы остаться на Марсе ?'] = request.form.get('ready', 'no')
    return render_template('answer.html', data=user_data)

if __name__ == '__main__':
    app.run(port=4005, host='127.0.0.1')