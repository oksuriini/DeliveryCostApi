from math import ceil

DISTANCE_BASE_FEE_CENTS = 200
DISTANCE_BASE_LIMIT_METERS = 1000
ADDITIONAL_DISTANCE_FEE_CENTS = 100
ADDITIONAL_DISTANCE_LIMIT_METERS = 500


def calculate_distance_fee(distance_in_meters: int) -> int:
    """
    Calculates distance fee.

    :param distance_in_meters: int, delivery distance in meters

    :return: int, calculated distance fee
    """
    distance_fee = 0
    if distance_in_meters <= DISTANCE_BASE_LIMIT_METERS:
        distance_fee = DISTANCE_BASE_FEE_CENTS
    else:
        distance_fee = DISTANCE_BASE_FEE_CENTS + (
            ceil(
                (
                    (distance_in_meters - DISTANCE_BASE_LIMIT_METERS)
                    / ADDITIONAL_DISTANCE_LIMIT_METERS
                )
            )
            * ADDITIONAL_DISTANCE_FEE_CENTS
        )
    return distance_fee
