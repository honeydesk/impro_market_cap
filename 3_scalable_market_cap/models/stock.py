from dataclasses import dataclass

@dataclass(frozen=True)
class Stock:
    symbol: str
    price_per_share: float
    total_shares: int

    def validate(self) -> None:
        if self.price_per_share < 0:
            raise ValueError("Price per share must be non-negative")

        if self.total_shares < 0:
            raise ValueError("Total shares must be non-negative")