from datetime import datetime


def validate_request_json(order_details) -> str:
    """
    Validate delivery order's values.
    parameter order_details must be in JSON format with correct keys.

    :param order_detail: Order details in JSON format
    format and keys:
    {
      "cart_value": integer,
      "delivery_distance": integer,
      "number_of_items": integer,
      "time": string
    }

    :returns: str, which indicates an issue if it has value. If string is empty, then there is no issue.
    """

    validation_string = ""

    if isinstance(order_details["cart_value"], int):
        if order_details["cart_value"] < 0:
            validation_string = "Order value can't be negative."
    else:
        validation_string = "Order value must be integer."

    if isinstance(order_details["delivery_distance"], int):
        if order_details["delivery_distance"] < 0:
            validation_string = "Delivery distance can't be negative."
    else:
        validation_string = "Delivery distance must be integer."

    if isinstance(order_details["number_of_items"], int):
        if order_details["number_of_items"] < 1:
            validation_string = "Number of items can't be zero."
    else:
        validation_string = "Number of items must be integer."

    if isinstance(order_details["time"], str):
        try:
            datetime.fromisoformat(order_details["time"])
        except:
            validation_string = "Given date and time format was invalid."
    else:
        validation_string = "Date must be a string"

    return validation_string
