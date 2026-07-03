# Binance Futures Testnet Trading Bot

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- CLI interface
- Input validation
- Logging
- Error handling

## Project Structure

trading_bot/
    bot/
        client.py
        orders.py
        validators.py
        logging_config.py
    cli.py
    requirements.txt
    README.md
    logs/

## Installation

1. Clone the repository

2. Create virtual environment

3. Install requirements

pip install -r requirements.txt

4. Create a .env file

API_KEY=your_api_key
SECRET_KEY=your_secret_key

## Usage

MARKET BUY

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

MARKET SELL

python cli.py --symbol BTCUSDT --side SELL --order_type MARKET --quantity 0.001

LIMIT BUY

python cli.py --symbol BTCUSDT --side BUY --order_type LIMIT --quantity 0.002 --price 30000

LIMIT SELL

python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.002 --price 130000

## Assumptions

- Uses Binance Futures Testnet
- LIMIT orders require a price
- MARKET orders ignore the price parameter

## Logging

Log files are created automatically inside the logs/ directory.