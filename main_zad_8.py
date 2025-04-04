import os
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/images'  # Папка для загрузки
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

class UploadForm(FlaskForm):
    image = FileField('Выберите изображение', validators=[DataRequired()])
    submit = SubmitField('Загрузить')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    default_image = 'mars_default.jpg'
    curr_img = default_image

    loaded_img = [f for f in os.listdir(app.config['UPLOAD_FOLDER'])
                 if allowed_file(f)]
    if loaded_img:
        curr_img = loaded_img[-1]

    if form.validate_on_submit():
        file = form.image.data
        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))

    return render_template('shablon_8_1.html', form=form, image=curr_img,
                         default_image=default_image)

if __name__ == '__main__':
    app.run(debug=True)