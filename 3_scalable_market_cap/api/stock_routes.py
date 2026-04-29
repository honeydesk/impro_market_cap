from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StockRequest(BaseModel):
    symbol: str
    price_per_share: float
    total_shares: int


@app.post("/market-cap")
def market_cap(stock: StockRequest):

    cap = stock.price_per_share * stock.total_shares

    return {
        "symbol": stock.symbol,
        "market_cap": cap
    }


@app.get("/calculate")
def calculate_market_cap(price_per_share: float, total_shares: int):
    if price_per_share < 0 or total_shares < 0:
        raise ValueError("Price per share and total shares must be positive values.")
    return price_per_share * total_shares