from calculations.cart_value_surcharge import calculate_cart_value_surchange
from calculations.distance_fee import calculate_distance_fee
from calculations.item_count_surcharge import calculate_item_count_surcharge
from calculations.rush_time_surcharge import calculate_rush_time_surcharge

DELIVERY_FEE_MAX_LIMIT = 1500


def calculate_full_delivery_fee(order_details) -> int:
    """
    Function that calculates entire delivery fee.
    Uses helper function to count delivery fee step by step.

    :param order_details: Order details in JSON format.

    :returns: int, delivery fee in cents.
    """

    delivery_fee_in_cents: int = 0

    delivery_fee_in_cents += calculate_cart_value_surchange(order_details["cart_value"])

    if delivery_fee_in_cents == -1:
        return 0

    delivery_fee_in_cents += calculate_distance_fee(order_details["delivery_distance"])

    delivery_fee_in_cents += calculate_item_count_surcharge(
        order_details["number_of_items"]
    )

    delivery_fee_in_cents = calculate_rush_time_surcharge(
        order_details["time"], delivery_fee_in_cents
    )

    if delivery_fee_in_cents > DELIVERY_FEE_MAX_LIMIT:
        return DELIVERY_FEE_MAX_LIMIT

    return delivery_fee_in_cents
