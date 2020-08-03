from flask import Flask, request
import pandas as pd
import tensorflow
from keras.models import load_model


app = Flask(__name__)


@app.route('/predictions')
def get_predictions():
    crop_type = request.args.get('crop_type')
    X = pd.get_dummies(crop_type)
    model = load_model('dnn_model')
    return model.predict(X)


if __name__ == '__main__':
    app.run()
