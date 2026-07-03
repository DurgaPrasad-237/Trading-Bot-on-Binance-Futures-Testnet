import argparse

from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_limit_order,
)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        type=validate_symbol,
        help="Trading pair (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        type=validate_side,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--order_type",
        required=True,
        type=validate_order_type,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=validate_quantity,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=validate_price,
        help="Price (required for LIMIT orders)"
    )

    args = parser.parse_args()

    # Validate LIMIT order price
    validate_limit_order(args.price, args.order_type)

    manager = OrderManager()

    if args.order_type == "MARKET":
        order = manager.place_market_order(
            symbol=args.symbol,
            side=args.side,
            quantity=args.quantity
        )

    else:
        order = manager.place_limit_order(
            symbol=args.symbol,
            side=args.side,
            quantity=args.quantity,
            price=args.price
        )

    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {args.side}")
    print(f"Type     : {args.order_type}")
    print(f"Quantity : {args.quantity}")

    if args.order_type == "LIMIT":
        print(f"Price    : {args.price}")

    print("\n========== ORDER RESPONSE ==========")
    print(f"Order ID      : {order['orderId']}")
    print(f"Status        : {order['status']}")
    print(f"Executed Qty  : {order.get('executedQty', 'N/A')}")
    print(f"Average Price : {order.get('avgPrice', 'N/A')}")

    print("\n✅ Order placed successfully!")


if __name__ == "__main__":
    main()