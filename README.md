# Impro Market Cap

A Python project demonstrating progressive improvement in code structure and scalability for calculating stock market capitalization. This project showcases three different implementations of the same functionality, from a simple script to a full-featured API.

## Project Overview

This project calculates **Market Capitalization** using the formula:
```
Market Cap = Price per Share × Total Number of Shares
```

It demonstrates three levels of code evolution:
- **Level 1**: Simple, straightforward implementation
- **Level 2**: Refactored with better structure and error handling
- **Level 3**: Scalable architecture with models, services, and REST API

## Project Structure

```
impro_market_cap/
├── 1_market_cap/                    # Simple implementation
│   └── 1_simple_market_cap.py       # Basic market cap calculation
├── 2_refactored_market_cap/         # Refactored implementation
│   ├── refactored_market_cap.py     # Improved structure with validation
│   ├── tests/
│   │   └── refactored_market_cap_test.py
│   └── __init__.py
├── 3_scalable_market_cap/           # Enterprise-ready architecture
│   ├── api/
│   │   ├── stock_routes.py          # FastAPI endpoints
│   │   └── __init__.py
│   ├── models/
│   │   ├── stock.py                 # Stock data model
│   │   └── __init__.py
│   ├── services/
│   │   ├── market_cap_service.py    # Business logic
│   │   └── __init__.py
│   ├── tests/
│   │   └── scalable_market_cap_tests.py
│   └── __init__.py
├── main.py                           # Entry point
├── scalable_market_cap_main.py      # Example usage of scalable version
├── run_stock_api.py                 # FastAPI server launcher
├── test_stock_api.py                # API testing
├── pyproject.toml                   # Project configuration and dependencies
├── LICENSE                          # Project license
└── README.md                        # This file
```

## Requirements

- **Python**: 3.12 or higher
- **Dependencies**: See `pyproject.toml`

### Main Dependencies

- `fastapi>=0.136.1` - Web framework for the REST API
- `uvicorn>=0.46.0` - ASGI server for FastAPI
- `pydantic>=2.13.3` - Data validation using Python type annotations
- `pytest>=9.0.3` - Testing framework
- `requests>=2.33.1` - HTTP client library
- `python-dotenv>=1.2.2` - Environment variable management

## Installation

1. **Clone the repository** (if not already done):
```bash
cd impro_market_cap
```

2. **Install dependencies** using pip:
```bash
pip install -e .
```

Or install specific packages:
```bash
pip install fastapi uvicorn pydantic pytest requests python-dotenv
```

3. **Verify installation**:
```bash
python -c "import fastapi; print(f'FastAPI version: {fastapi.__version__}')"
```

## Execution Guide

### Option 1: Simple Market Cap Calculation

Run the simple calculation example:

```bash
python 1_market_cap/1_simple_market_cap.py
```

**Output**:
```
Market Capitalization: $56700000.0
```

### Option 2: Scalable Market Cap (Command Line)

Run the scalable implementation example:

```bash
python scalable_market_cap_main.py
```

**Output**:
```
AAPL Market Cap: $56,700,000.00
```

### Option 3: FastAPI REST API Server

Start the FastAPI server for programmatic access:

```bash
python run_stock_api.py
```

**Server Output**:
```
🚀 Starting FastAPI server...
📍 API URL: http://localhost:8000
📚 Docs: http://localhost:8000/docs
```

The server will start at `http://localhost:8000` with interactive API documentation.

#### Available API Endpoints

1. **POST /market-cap** - Calculate market cap for a stock
   ```bash
   curl -X POST "http://localhost:8000/market-cap" \
     -H "Content-Type: application/json" \
     -d '{
       "symbol": "AAPL",
       "price_per_share": 150.25,
       "total_shares": 15000000
     }'
   ```

   **Response**:
   ```json
   {
     "symbol": "AAPL",
     "market_cap": 2253750000.0
   }
   ```

2. **GET /calculate** - Simple query-based calculation
   ```bash
   curl "http://localhost:8000/calculate?price_per_share=150.25&total_shares=15000000"
   ```

   **Response**: `2253750000.0`

3. **GET /docs** - Interactive API documentation (Swagger UI)
   - Open `http://localhost:8000/docs` in your browser

4. **GET /redoc** - Alternative API documentation (ReDoc)
   - Open `http://localhost:8000/redoc` in your browser

## Testing

### Run All Tests

```bash
pytest
```

### Run Tests for Specific Module

```bash
# Test refactored version
pytest 2_refactored_market_cap/tests/

# Test scalable version
pytest 3_scalable_market_cap/tests/
```

### Run Tests with Verbose Output

```bash
pytest -v
```

### Run Tests with Coverage Report

```bash
pytest --cov=3_scalable_market_cap --cov=2_refactored_market_cap
```

## Architecture Comparison

| Aspect | Level 1 | Level 2 | Level 3 |
|--------|---------|---------|----------|
| **Structure** | Simple function | Modular functions | Service + Model + API |
| **Error Handling** | Basic try-catch | Custom validation | Pydantic validation |
| **Reusability** | Low | Medium | High |
| **Testing** | Manual | Unit tests | Comprehensive tests |
| **Scalability** | Limited | Moderate | Enterprise-ready |
| **API Support** | None | None | REST API with docs |

## Development Workflow

1. **Start the API server**: `python run_stock_api.py`
2. **In another terminal, test the API**: Use curl or the interactive docs at `http://localhost:8000/docs`
3. **Run tests**: `pytest`
4. **Make changes** and iterate

## Example Usage in Python

```python
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent / "3_scalable_market_cap"))

from services.market_cap_service import MarketCapService
from models.stock import Stock

# Create a stock
stock = Stock(
    symbol="GOOGL",
    price_per_share=140.50,
    total_shares=12_800_000
)

# Calculate market cap
market_cap = MarketCapService.calculate(stock)
print(f"{stock.symbol} Market Cap: ${market_cap:,.2f}")
```

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## Contributing

Contributions are welcome! Please ensure:
- Code follows Python best practices
- All tests pass: `pytest`
- New features include appropriate tests

## Questions or Issues?

For questions or issues, please refer to the project structure and test examples for usage patterns.
