import json
import websocket
import logging
import sys
# logging.basicConfig(filename='output.log', level=logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class BinanceConnector:
    def __init__(self):
        self.socket = 'wss://stream.binance.com:9443/ws'
        self.btcusdt_candlesticks = list()
        self.ethusdt_candlesticks = list()
        self.bnbbtc_candlesticks = list()

    # Subscribing to binance receive the required minute candlesticks for pairs
    def on_open(self, ws):
        logging.info('opened')
        subscribe_message = {
            "method": "SUBSCRIBE",
            "params":
            [
                "btcusdt@kline_1m",
                "ethusdt@kline_1m",
                "bnbbtc@kline_1m"
            ],
            "id": 1
        }
        ws.send(json.dumps(subscribe_message))

    # Processing the input message and calculating the moving average for each pair
    def on_message(self, ws, message):
        received_json = json.loads(message)
        self.moving_average(received_json['s'], received_json['k']['c'])

    def on_close(self, ws):
        logging.info("closed connection")


    def run(self):
        ws = websocket.WebSocketApp(self.socket,
                                    on_open=self.on_open,
                                    on_message=self.on_message,
                                    on_close=self.on_close)
        ws.run_forever()
    # Calculating moving average for last 10 one minute candlesticks for each pair
    def moving_average(self, s, c):
        if s == 'BTCUSDT':
            if len(self.btcusdt_candlesticks) < 9:
                self.btcusdt_candlesticks.append(float(c))
            elif len(self.btcusdt_candlesticks) == 9:
                self.btcusdt_candlesticks.append(float(c))
                moving_average = sum(self.btcusdt_candlesticks) / 10
                self.btcusdt_candlesticks = list()
                logging.info('Moving Average BTCUSDT for last 10 candlesticks = '
                             + str(moving_average))
                return moving_average
        elif s == 'ETHUSDT':
            if len(self.ethusdt_candlesticks) < 9:
                self.ethusdt_candlesticks.append(float(c))
            elif len(self.ethusdt_candlesticks) == 9:
                self.ethusdt_candlesticks.append(float(c))
                moving_average = sum(self.ethusdt_candlesticks) / 10
                self.ethusdt_candlesticks = list()
                logging.info('Moving Average ETHUSDT for last 10 candlesticks = '
                             + str(moving_average))
                return moving_average
        elif s == 'BNBBTC':
            if len(self.bnbbtc_candlesticks) < 9:
                self.bnbbtc_candlesticks.append(float(c))
            elif len(self.bnbbtc_candlesticks) == 9:
                self.bnbbtc_candlesticks.append(float(c))
                moving_average = sum(self.bnbbtc_candlesticks) / 10
                self.bnbbtc_candlesticks = list()
                logging.info('Moving Average BNBBTC for last 10 candlesticks = '
                             + str(moving_average))
                return moving_average


binance_connector = BinanceConnector()
if __name__ == "__main__":
    binance_connector.run()



