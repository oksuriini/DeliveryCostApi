# Wolt backend trainee assignment:

The assignment was to create an API backend to calculate delivery fee based on order information that is sent to the API's endpoint.
API had one endpoint that takes POST requests, where the order information is within request's body in JSON format, and it responds with body that has the delivery fee in JSON format.

## Install instructions:

Extract the zip file.

Change the directory to the extracted folder: `cd <zipname>`

Create virtual environment:
`python -m venv .venv`

Activate virtual environment:
Windows: `.\.venv\Scripts\activate.bat`
Linux / MacOS: `source ./.venv/bin/activate`

Install required packages with pip to virtual environment:
`pip install -r requirements.txt`

The program should be usable after these steps.

## Usage instructions

From root folder "<zipname>" you can run the API itself, or the tests with following commands:

Run API:
Type in terminal / console: `python ./src/app.py`

Terminal / Console should inform that the server is running on "http://127.0.0.1:5000".
If you get a line that says port 5000 is in use by another program, you can close that program or change the port that flask uses by changing the value of FLASK_PORT in app.py file.

You can make POST requests that hold the order information in the body to the API at endpoint `/deliveryfee`.

### Postman example:

Set URL to `http://127.0.0.1:5000`, and the method to POST.
Full URL should be "http://127.0.0.1:5000/deliveryfee"
Set body to raw and from dropdown menu that says "Text" select option "JSON".

Example1:
Set the body as following:
{"cart_value": 850, "delivery_distance": 1273, "number_of_items": 6, "time": "2024-01-26T16:32:11Z"}

API should response with status code 200, and body:
{"delivery_fee": 660}

Example2:
Request:
`{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}`
Response:
`{"delivery_fee": 710}`

### curl example:

Request:
`curl -X POST http://127.0.0.1:5000/deliveryfee -H "Content-Type: application/json" -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}'`

Response:
`{"delivery_fee": 710}`

## Testing

Unit test are located in the root folder's folder "tests" in file "tests.py"

Unit tests:
`python -m unittest ./tests/tests.py`
