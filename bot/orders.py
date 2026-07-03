from bot.client import BinanceClient
from binance.exceptions import BinanceAPIException
from binance.enums import *
from bot.logging_config import get_logger

logger = get_logger()

class OrderManager:
    def __init__(self):
        self.client = BinanceClient().get_client()
       
    
    def place_market_order(self,symbol:str,side:str,quantity:float):
        """place an Market order on the Binance Futures Testnet"""

        logger.info(
            f"MARKET ORDER REQUEST | "
            f"Symbol={symbol} | "
            f"Side={side} | "
            f"Quantity={quantity}"
        )
        
        try:
            order = self.client.futures_create_order(
                symbol = symbol.upper(),
                side = side.upper(),
                type = ORDER_TYPE_MARKET,
                quantity = quantity
            )

            logger.info(
                f"MARKET ORDER RESPONSE | "
                f"OrderID={order['orderId']} | "
                f"Status={order['status']} | "
                f"ExecutedQty={order.get('executedQty')} | "
                f"AvgPrice={order.get('avgPrice', 'N/A')}"
            )

            return order

        except BinanceAPIException as e:
            logger.error(f"MARKET ORDER ERROR | {e.message}")
            raise
        except Exception as e:
            logger.exception("Unexpected error while placing MARKET order")
            raise

    def place_limit_order(self,symbol:str,side:str,price:float,quantity:float):
        """place an limit order on the binance futures testnet"""

        logger.info(
            f"LIMIT ORDER REQUEST | "
            f"Symbol={symbol} | "
            f"Side={side} | "
            f"Quantity={quantity} | "
            f"Price={price}"
        )

        try:
            order = self.client.futures_create_order(
                symbol = symbol.upper(),
                side = side.upper(),
                type = ORDER_TYPE_LIMIT,
                price = price,
                timeInForce = TIME_IN_FORCE_GTC,
                quantity = quantity,          
            )

            logger.info(
                f"LIMIT ORDER RESPONSE | "
                f"OrderID={order['orderId']} | "
                f"Status={order['status']} | "
                f"ExecutedQty={order.get('executedQty')} | "
                f"AvgPrice={order.get('avgPrice', 'N/A')}"
            )
            return order
        except BinanceAPIException as e:
            logger.error(f"LIMIT ORDER ERROR | {e.message}")
            raise
        except Exception as e:
            logger.exception("Unexpected error while placing LIMIT order")
            raise
        
        

    