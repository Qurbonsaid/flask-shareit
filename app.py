import os

from flask import Flask, send_from_directory, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 * 1024
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/')
def share():
    files = os.listdir(os.path.join(app.root_path, app.config['UPLOAD_FOLDER']))
    return render_template('share.html', files=files)


@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    for f in files:
        f.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    return redirect(url_for('share'))


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)  # You can change the IP and port yourself
