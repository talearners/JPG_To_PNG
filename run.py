from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from os.path import join
from PIL import Image
from time import time
from hashlib import md5


UPLOAD_FOLDER = "./static/media/"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        fileObject = request.files['file']
        filename = secure_filename(md5(str(time()).encode()).hexdigest()+'.png')
        filename = join(app.config["UPLOAD_FOLDER"],filename)
        fileObject = Image.open(fileObject)
        fileObject.save(filename)
        return  render_template("index.html",file_url=filename)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)