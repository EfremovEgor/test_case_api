import unittest
import requests
from settings import API_KEY, THIS_API_URL


class TestCurrencyExchange(unittest.TestCase):
    def get_currency_response(self, from_, to):
        url = "https://api.freecurrencyapi.com/v1/latest"
        headers = {"apikey": API_KEY}
        params = {"base_currency": from_, "currencies": [to]}
        response = requests.get(url, headers=headers, params=params)
        return response

    def test_expected_behaviour(self):
        data_expected = self.get_currency_response("USD", "RUB").json()

        data_expected = data_expected["data"]["RUB"]

        data_got = requests.get(
            THIS_API_URL + "/api/rates?from=USD&to=RUB&value=1"
        ).json()["result"]
        print(data_got)
        self.assertAlmostEqual(data_expected, data_got, 3)

    def test_wrong_parameters(self):
        data_got = requests.get(THIS_API_URL + "/api/rates?from=USD&to=RU&value=1")
        self.assertTrue(not data_got.ok)


if __name__ == "__main__":
    unittest.main()
