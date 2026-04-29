from models.stock import Stock

class MarketCapService:

    @staticmethod
    def calculate(stock: Stock) -> float:
        stock.validate()
        return stock.price_per_share * stock.total_shares