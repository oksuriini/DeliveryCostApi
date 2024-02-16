SURCHARGE_COUNT_LIMIT: int = 4
SURCHARGE_PER_ITEM_CENTS: int = 50
BULK_COUNT_LIMIT: int = 13
BULK_FEE: int = 120


def calculate_item_count_surcharge(item_count: int) -> int:
    """
    Calculates surcharge if item count is over designated limit.

    :param item_count: int, amount of items in cart

    :return: int, calculated surcharge
    """
    surcharge: int = 0

    if item_count <= SURCHARGE_COUNT_LIMIT:
        surcharge = 0
    elif SURCHARGE_COUNT_LIMIT < item_count < BULK_COUNT_LIMIT:
        surcharge = (item_count - SURCHARGE_COUNT_LIMIT) * SURCHARGE_PER_ITEM_CENTS
    elif item_count >= BULK_COUNT_LIMIT:
        surcharge = (
            (item_count - SURCHARGE_COUNT_LIMIT) * SURCHARGE_PER_ITEM_CENTS
        ) + BULK_FEE
    else:
        pass

    return surcharge
