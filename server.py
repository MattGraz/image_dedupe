import subprocess
import json
import scipy
import time
import numpy as np
from flask import Flask, Response

BASE_DIR = "/home/its-an-avacado/plex/data/pictures"


app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template('index.html')


# @app.route("/echo", methods=['POST'])
# def echo():
#     command = request.form['text']
#     subprocess.call([command])
#     # return request.form['text'] + " Command executed via subprocess"
#     return index()


# @app.route("/calc", methods=['POST'])
# def calc():
#     subprocess.call('calc.exe')
#     return index()


# @app.route("/test", methods=['POST'])
# def test():
#     while True:
#         subprocess.call('calc.exe')


# def stream_template(template_name, **context):
#     app.update_template_context(context)
#     t = app.jinja_env.get_template(template_name)
#     rv = t.stream(context)
#     return rv


@app.route('/new_image')
def generate_image():
    def generate():
        for i in range(10):
            noise_image = np.random.uniform(
                0, 256, (224, 224, 3)).astype('float32')
            scipy.misc.imsave('out/' + str(i) + '.jpg', noise_image)
            time.sleep(1)
            yield(str(i) + '.jpg')

    return Response(stream_template('templates/image.html', data=generate()))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
