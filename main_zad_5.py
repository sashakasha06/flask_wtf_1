from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def listing():
    return render_template('shablon_5_1.html')
@app.route('/distribution', methods=['POST'])
def distribution():
    listin = f'{request.form.get('astro_id', '')}, {request.form.get('astro_pass', '')}, {request.form.get('cap_id', '')}, {request.form.get('cap_pass', '')}'
    dostup = [name.strip() for name in listin.split(',') if name.strip()]
    return render_template('shablon_5_2.html', astronauts=dostup)

if __name__ == '__main__':
    app.run(debug=True)