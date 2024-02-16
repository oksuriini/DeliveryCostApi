from src.calculations.cart_value_surcharge import (
    calculate_cart_value_surchange,
    SMALL_SURCHARGE_LIMIT,
)
from src.calculations.distance_fee import (
    ADDITIONAL_DISTANCE_FEE_CENTS,
    ADDITIONAL_DISTANCE_LIMIT_METERS,
    DISTANCE_BASE_FEE_CENTS,
    DISTANCE_BASE_LIMIT_METERS,
    calculate_distance_fee,
)
from src.calculations.item_count_surcharge import (
    BULK_COUNT_LIMIT,
    BULK_FEE,
    SURCHARGE_COUNT_LIMIT,
    SURCHARGE_PER_ITEM_CENTS,
    calculate_item_count_surcharge,
)
from src.calculations.rush_time_surcharge import (
    RUSH_HOUR_MULTIPLIER,
    calculate_rush_time_surcharge,
)

import unittest


class TestCartvalueFunctions(unittest.TestCase):
    def test_surcharge(self):
        """
        Test that surcharge is counted
        """
        self.assertEqual(
            calculate_cart_value_surchange(890),
            SMALL_SURCHARGE_LIMIT - 890,
            "Function should return surcharge that equals: SMALL_SURCHARGE_LIMIT - <INPUT>.",
        )

    def test_surcharge_at_limit(self):
        """
        Test that surcharge is 0 at surcharge limit
        """
        self.assertEqual(
            calculate_cart_value_surchange(SMALL_SURCHARGE_LIMIT),
            0,
            "At SMALL_SURCHARGE_LIMIT value, surcharge should always be 0.",
        )

    def test_surcharge_above_limit(self):
        """
        Test that surcharge is 0 above surcharge limit
        """
        self.assertEqual(
            calculate_cart_value_surchange(SMALL_SURCHARGE_LIMIT + 250),
            0,
            "At higher cart value than SMALL_SURCHARGE_LIMIT, surcharge should always be 0.",
        )

    def test_negative_price(self):
        """
        Test that surchage is defaulted to limit when cart value is negative
        """
        self.assertEqual(
            calculate_cart_value_surchange(-100),
            SMALL_SURCHARGE_LIMIT,
            "Negative cart value should not be possible, but in case it happens, default surcharge to SMALL_SURCHARGE_LIMIT.",
        )


class TestDistanceFeeFunctions(unittest.TestCase):
    def test_fee_below_limit(self):
        """
        Test that distance fee is correct below the base limit
        """
        self.assertEqual(
            calculate_distance_fee(DISTANCE_BASE_LIMIT_METERS - 1),
            DISTANCE_BASE_FEE_CENTS,
            "Distance surcharge should be only base fee, even below the DISTANCE_BASE_LIMIT_METERS.",
        )

    def test_fee_at_limit(self):
        """
        Test that distance fee is correct at the base limit
        """
        self.assertEqual(
            calculate_distance_fee(DISTANCE_BASE_LIMIT_METERS),
            DISTANCE_BASE_FEE_CENTS,
            "Distance surcharge should be only base fee at DISTANCE_BASE_LIMIT_METERS.",
        )

    def test_fee_beyond_limit_flat(self):
        """
        Test that distance fee is correct when distance has no remainder
        """
        self.assertEqual(
            calculate_distance_fee(
                DISTANCE_BASE_LIMIT_METERS + (ADDITIONAL_DISTANCE_LIMIT_METERS * 4)
            ),
            (DISTANCE_BASE_FEE_CENTS + (ADDITIONAL_DISTANCE_FEE_CENTS * 4)),
            "Distance surcharge should follow formula above.",
        )

    def test_fee_beyond_limit_nonflat(self):
        """
        Test that distance fee has a remainder
        """
        self.assertEqual(
            calculate_distance_fee(
                DISTANCE_BASE_LIMIT_METERS
                + (ADDITIONAL_DISTANCE_LIMIT_METERS * 5)
                + (
                    ADDITIONAL_DISTANCE_LIMIT_METERS
                    - int((ADDITIONAL_DISTANCE_LIMIT_METERS * 0.25))
                )
            ),
            (DISTANCE_BASE_FEE_CENTS + (ADDITIONAL_DISTANCE_FEE_CENTS * 6)),
            "Distance surcharge should follow formula above, even when the distance division doesn't return whole number. Pricing is based on steps that are rounded up.",
        )


class TestItemCountFeeFunctions(unittest.TestCase):
    def test_surcharge_below_limit(self):
        """
        Test item count surcharge when below limit
        """
        self.assertEqual(
            calculate_item_count_surcharge(SURCHARGE_COUNT_LIMIT - 2),
            0,
            "Item count surcharge should be zero below surcharge count",
        )

    def test_surcharge_at_limit(self):
        """
        Test item count surcharge at limit
        """
        self.assertEqual(
            calculate_item_count_surcharge(SURCHARGE_COUNT_LIMIT),
            0,
            "Item count surcharge should be zero when at surcharge count.",
        )

    def test_surcharge_one_over_limit(self):
        """
        Test item count surcharge one above limit
        """
        self.assertEqual(
            calculate_item_count_surcharge(SURCHARGE_COUNT_LIMIT + 1),
            SURCHARGE_PER_ITEM_CENTS,
            "Surcharge should be exactly SURCHARGE_PER_ITEM_CENTS",
        )

    def test_surcharge_four_over_limit(self):
        """
        Test item count surcharge 4 over limit
        """
        self.assertEqual(
            calculate_item_count_surcharge(SURCHARGE_COUNT_LIMIT + 4),
            SURCHARGE_PER_ITEM_CENTS * 4,
            "Surcharge should be exactly SURCHARGE_PER_ITEM_CENTS * 4",
        )

    def test_surcharge_below_bulk_count(self):
        """
        Test item count surcharge one item below bulk count
        """
        self.assertEqual(
            calculate_item_count_surcharge(BULK_COUNT_LIMIT - 1),
            (BULK_COUNT_LIMIT - 1 - SURCHARGE_COUNT_LIMIT) * SURCHARGE_PER_ITEM_CENTS,
            "Surcharge should exactly the amount above, so one below bulk count.",
        )

    def test_surcharge_at_bulk_count(self):
        """
        Test item count surcharge at bulk count
        """
        self.assertEqual(
            calculate_item_count_surcharge(BULK_COUNT_LIMIT),
            ((BULK_COUNT_LIMIT - SURCHARGE_COUNT_LIMIT) * SURCHARGE_PER_ITEM_CENTS)
            + BULK_FEE,
            "Surcharge should be exactly at bulk fee count",
        )

    def test_surcharge_above_bulk_count(self):
        """
        Test item count surcharge above bulk count
        """
        self.assertEqual(
            calculate_item_count_surcharge(BULK_COUNT_LIMIT + 6),
            (BULK_COUNT_LIMIT + 6 - SURCHARGE_COUNT_LIMIT) * SURCHARGE_PER_ITEM_CENTS
            + BULK_FEE,
            "Surcharge should be bulk fee and additional items over bulk count",
        )


class TestRushTimeFeeFunctions(unittest.TestCase):
    def test_active_date_inactive_time(self):
        """
        Test active day during inactive time
        """
        self.assertEqual(
            calculate_rush_time_surcharge("2023-11-10T12:26:50Z", 270),
            270,
            "Price should not change on active date when rush hour is not active",
        )

    def test_inactive_date_active_time(self):
        """
        Test inactive day during active time
        """
        self.assertEqual(
            calculate_rush_time_surcharge("2023-11-05T16:26:50Z", 270),
            270,
            "Price should not change on inactive date when rush hour is active",
        )

    def test_active_date_active_time(self):
        """
        Test active date during active time"""
        self.assertEqual(
            calculate_rush_time_surcharge("2023-05-05T17:35:50Z", 270),
            270 * RUSH_HOUR_MULTIPLIER,
            "Price should not change on inactive date when rush hour is active",
        )
