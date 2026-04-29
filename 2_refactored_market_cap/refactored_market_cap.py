import logging
from typing import Union

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def calculate_market_cap(price_per_share: Union[int, float], total_shares: int) -> float:
    """
    Calculate market capitalization.

    Args:
        price_per_share (float): Price of a single share.
        total_shares (int): Total number of outstanding shares.

    Returns:
        float: Market capitalization.

    Raises:
        ValueError: If inputs are negative.
        TypeError: If inputs are not numeric.
    """

    if not isinstance(price_per_share, (int, float)):
        raise TypeError("price_per_share must be numeric")

    if not isinstance(total_shares, int):
        raise TypeError("total_shares must be an integer")

    if price_per_share < 0 or total_shares < 0:
        raise ValueError("Inputs must be non-negative")

    return price_per_share * total_shares


def main() -> None:
    """Entry point for script execution."""

    price_per_share = 56.7
    total_shares = 1_000_000

    try:
        market_cap = calculate_market_cap(price_per_share, total_shares)
        logger.info("Market Capitalization: $%.2f", market_cap)

    except (ValueError, TypeError) as err:
        logger.error("Failed to calculate market cap: %s", err)


if __name__ == "__main__":
    main()