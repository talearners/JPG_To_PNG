from click import File
from flask import (
    Flask,
    render_template,
    request,
    url_for
)
from werkzeug.utils import secure_filename
from hashlib import md5
from os.path import join
from time import time
from PIL import Image


# start Flask App 

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = './static/media/'

# Start Flask Route

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":

        option = request.form["options"]
        FileObject = request.files['file']
        mimetype = FileObject.mimetype

        if FileObject.mimetype == "image/jpeg" and option == "PNG":
            filename = join(app.config["UPLOAD_FOLDER"],
            secure_filename(md5(str(time()).encode()).hexdigest()+'.png'))
            FileObject = Image.open(FileObject)
            FileObject.save(filename)
            return render_template('index.html',filename=filename)

        elif FileObject.mimetype == "image/png" and option == "JPG":
            filename = join(app.config["UPLOAD_FOLDER"],
            secure_filename(md5(str(time()).encode()).hexdigest()+'.jpg'))
            FileObject = Image.open(FileObject)
            FileObject = FileObject.convert("RGB")  # convert into JPG 
            FileObject.save(filename)
            return render_template('index.html',filename=filename)

        else:
            return render_template('index.html',mimetype=mimetype)  # For Extra Security

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)