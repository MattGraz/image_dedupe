from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def show_index():
    full_filename = '/home/its-an-avacado/repos/image_dedupe/out/10.jpg'
    # return render_template("index.html", user_image=full_filename)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
