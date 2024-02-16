import logging

NO_DELIVERYFEE_LIMIT = 20000
SMALL_SURCHARGE_LIMIT = 1000


def calculate_cart_value_surchange(cart_value_cents: int) -> int:
    """
    Calculates surcharge if cart value is less than limit, or returns -1 if cart value is equal or above free delivery limit.

    :param cart_value_cents: int, value of cart in cents

    :return: int, `-1` if delivery is free, otherwise calculated surcharge
    """
    surcharge = 0

    if 0 <= cart_value_cents < SMALL_SURCHARGE_LIMIT:
        surcharge: int = SMALL_SURCHARGE_LIMIT - cart_value_cents
    elif cart_value_cents >= NO_DELIVERYFEE_LIMIT:
        surcharge = -1
    elif cart_value_cents < 0:
        logging.warning(
            "Negative cart value should NOT be possible, defaulting to SMALL_SURCHARGE_LIMIT"
        )
        surcharge = SMALL_SURCHARGE_LIMIT

    return surcharge
