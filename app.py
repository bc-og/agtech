from flask import Flask, request
import tensorflow
from keras.models import load_model


app = Flask(__name__)


@app.route('/predictions')
def get_predictions():
    crop_type = request.args.get('crop_type')
    model = load_model('dnn_model')
    return []


if __name__ == '__main__':
    app.run()
