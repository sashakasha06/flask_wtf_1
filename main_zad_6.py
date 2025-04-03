from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def listing():
    return render_template('shablon_6_2.html')
@app.route('/distribution', methods=['POST'])
def distribution():
    astronauts_str = request.form.get('motivation', '')
    astronauts = [name.strip() for name in astronauts_str.split(',') if name.strip()]
    return render_template('distribution.html', astronauts=astronauts)
if __name__ == '__main__':
    app.run(debug=True)