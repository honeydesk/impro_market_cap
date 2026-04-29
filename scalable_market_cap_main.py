import sys
from pathlib import Path

# Add the 3_scalable_market_cap directory to the path
sys.path.insert(0, str(Path(__file__).parent / "3_scalable_market_cap"))

from services.market_cap_service import MarketCapService
from models.stock import Stock

def main():

    apple = Stock(
        symbol="AAPL",
        price_per_share=56.7,
        total_shares=1_000_000
    )

    market_cap = MarketCapService.calculate(apple)

    print(f"{apple.symbol} Market Cap: ${market_cap:,.2f}")


if __name__ == "__main__":
    main()