from flask import Flask, request
from flask.helpers import abort
from delivery_fee import calculate_full_delivery_fee
from validators.validator import validate_request_json

FLASK_HOST = "127.0.0.1"
FLASK_PORT = 5000

app = Flask(__name__)


@app.post("/deliveryfee")
def calculate_delivery_fee():
    delivery_fee = 0
    validation_string = ""
    order_details = {}

    # Validate request body and then calculate delivery_fee
    if request.is_json:
        order_details = request.get_json()
        validation_string = validate_request_json(order_details)
        if validation_string == "":
            delivery_fee = calculate_full_delivery_fee(order_details)
        else:
            abort(400, validation_string)
    else:
        abort(400, "JSON request was invalid.")

    response = {"delivery_fee": delivery_fee}

    return response


app.run(FLASK_HOST, FLASK_PORT)
