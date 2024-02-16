from datetime import datetime

# Add weekdays on which rush hour is active, Monday = 1, Tuesday = 2 (...) Sunday = 7
RUSH_HOUR_WEEKDAYS = (5,)

RUSH_HOUR_TIME_START = 15
RUSH_HOUR_TIME_END = 19

RUSH_HOUR_MULTIPLIER = 1.2


def calculate_rush_time_surcharge(order_time: str, delivery_fee_in_cents: int) -> int:
    """
    Calculates rush time surcharge if applicable.

    :param order_time: str, order time in UTC in ISO format
    :param delivery_fee_in_cents: int, current delivery fee in cents

    :return: int, delivery fee with added surcharge
    """

    order_weekday_iso = datetime.fromisoformat(order_time).isoweekday()
    order_time_iso = datetime.fromisoformat(order_time).hour

    if order_weekday_iso in RUSH_HOUR_WEEKDAYS:
        if RUSH_HOUR_TIME_START <= order_time_iso <= RUSH_HOUR_TIME_END:
            delivery_fee_in_cents = int(delivery_fee_in_cents * RUSH_HOUR_MULTIPLIER)

    return delivery_fee_in_cents
