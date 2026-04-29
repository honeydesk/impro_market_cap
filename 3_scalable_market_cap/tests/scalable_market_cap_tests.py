import sys
from pathlib import Path
import pytest

# Add parent directory to path so we can import the module
sys.path.insert(0, str(Path(__file__).parent.parent))

from services.market_cap_service import MarketCapService
from models.stock import Stock

apple = Stock(
        symbol="AAPL",
        price_per_share=56.7,
        total_shares=1_000_000
    )

def test_market_cap():
    assert MarketCapService.calculate(apple) == 56700000.0


def test_negative_inputs():
    with pytest.raises(ValueError):
        MarketCapService.calculate(Stock("AAPL", -56.7, 1_000_000))


def test_invalid_type():
    with pytest.raises(TypeError):
        MarketCapService.calculate(Stock("AAPL", "56.7", 1_000_000))