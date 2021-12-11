import unittest
from binance_connector import BinanceConnector


class TestBinanceConnector(unittest.TestCase):
    def test_calculating(self):
        moving_average = 0
        for i in range(0, 10):
            binance_connector = BinanceConnector()
            moving_average = binance_connector.moving_average('BTCUSDT', '10')
        self.assertEqual(moving_average, 10.0)

    def test_calculating_false_name(self):
        moving_average = 0
        for i in range(0, 10):
            binance_connector = BinanceConnector()
            moving_average = binance_connector.moving_average('TEST', '1')
        self.assertEqual(moving_average, None)

    def test_calculating_false_value(self):
        moving_average = 0
        with self.assertRaises(ValueError):
            for i in range(0, 10):
                binance_connector = BinanceConnector()
                moving_average = binance_connector.moving_average('ETHUSDT', 'a')

if __name__ == "__main__":
    unittest.main()
