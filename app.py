from flask import Flask, request

app = Flask(__name__)


@app.route('/predictions')
def get_predictions():
    crop_type = request.args.get('crop_type')
    return []


if __name__ == '__main__':
    app.run()
