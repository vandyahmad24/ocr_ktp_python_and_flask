from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import cv2
import os
import pytesseract

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)

@app.route('/')
def index():
    return render_template("index.html")
    # return redirect(url_for('about'))

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():

   if request.method == 'POST':


      # f = request.files['file']
      # f.save(secure_filename(f.filename))
      # namefile = f.filename

      latestfile = request.files['file']
      full_filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(latestfile.filename))
      latestfile.save(full_filename)
      namefile = latestfile.filename


      img = cv2.imread(namefile)
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
      result = pytesseract.image_to_string((threshed), lang="ind")
      hasil = [result, namefile]
      print(hasil)
      return render_template("hasil.html", hasil = hasil)





if __name__ == '__main__':
    app.run(debug=True, port=5000)