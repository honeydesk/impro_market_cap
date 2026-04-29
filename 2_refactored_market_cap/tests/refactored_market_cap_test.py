import sys
from pathlib import Path
import pytest

# Add parent directory to path so we can import the module
sys.path.insert(0, str(Path(__file__).parent.parent))

from refactored_market_cap import calculate_market_cap

def test_market_cap():
    assert calculate_market_cap(10, 100) == 1000


def test_negative_inputs():
    with pytest.raises(ValueError):
        calculate_market_cap(-10, 100)


def test_invalid_type():
    with pytest.raises(TypeError):
        calculate_market_cap("10", 100)