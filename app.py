from flask import Flask, request
import numpy as np
import keras
from keras.models import load_model


app = Flask(__name__)


@app.route('/predictions', methods=['POST'])
def get_predictions():
    predicted_crop = ''
    observations = create_observations()
    observations = observations.reshape(1, 54)

    preds = produce_predictions(observations)
    predicted_crop = get_crop_category(predicted_crop, preds)
    return {'crop': predicted_crop}


def get_crop_category(predicted_crop, preds):
    max_index = np.argmax(preds)
    if max_index == 0:
        predicted_crop = 'Canola'
    elif max_index == 1:
        predicted_crop = 'Cereals'
    elif max_index == 2:
        predicted_crop = 'Grass'
    elif max_index == 3:
        predicted_crop = 'Legumes'
    else:
        predicted_crop = 'Others'
    return predicted_crop


def produce_predictions(observations):
    model = load_model('dnn_model')
    pred = model.predict(observations)
    return pred


def create_observations():
    observations = np.array([0 for _ in range(54)])
    request_body = request.get_json()
    selections = request_body['selections']
    for i in selections:
        observations[i] = 1
    return observations


if __name__ == '__main__':
    app.run()
