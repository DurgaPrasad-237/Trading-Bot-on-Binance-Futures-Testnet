import os
from dotenv import load_dotenv
from binance.client import Client
load_dotenv()   

class BinanceClient:
    def __init__(self):

        self.API_KEY = os.getenv("API_KEY")
        self.SECRET_KEY = os.getenv("SECRET_KEY")

        if not self.API_KEY or not self.SECRET_KEY:
            raise ValueError("API_KEY and SECRET_KEY must be set in the .env file")
      
    
    def get_client(self) -> Client:
        """Returns a configured Binance Futures Testnet client."""
        client = Client(self.API_KEY,self.SECRET_KEY)
        FUTURES_TESTNET_URL = "https://testnet.binancefuture.com/fapi"
        client.FUTURES_URL = FUTURES_TESTNET_URL
        return client
    

    