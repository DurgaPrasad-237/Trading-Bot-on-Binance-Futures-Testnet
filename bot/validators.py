import argparse


def validate_symbol(symbol: str) -> str:
    """Validate the trading symbol."""

    symbol = symbol.upper().strip()

    if len(symbol) < 3:
        raise argparse.ArgumentTypeError(
            "Symbol must contain at least 3 characters."
        )

    return symbol


def validate_side(side: str) -> str:
    """Validate order side."""

    side = side.upper().strip()

    if side not in ("BUY", "SELL"):
        raise argparse.ArgumentTypeError(
            "Side must be either BUY or SELL."
        )

    return side


def validate_order_type(order_type: str) -> str:
    """Validate order type."""

    order_type = order_type.upper().strip()

    if order_type not in ("MARKET", "LIMIT"):
        raise argparse.ArgumentTypeError(
            "Order type must be either MARKET or LIMIT."
        )

    return order_type


def validate_quantity(quantity: str) -> float:
    """Validate quantity."""

    try:
        quantity = float(quantity)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Quantity must be a valid number."
        )

    if quantity <= 0:
        raise argparse.ArgumentTypeError(
            "Quantity must be greater than 0."
        )

    return quantity


def validate_price(price: str) -> float:
    """Validate price."""

    try:
        price = float(price)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Price must be a valid number."
        )

    if price <= 0:
        raise argparse.ArgumentTypeError(
            "Price must be greater than 0."
        )

    return price


def validate_limit_order(price, order_type):
    """
    LIMIT orders require a price.
    MARKET orders do not.
    """

    if order_type == "LIMIT" and price is None:
        raise ValueError(
            "LIMIT orders require --price."
        )

    return True