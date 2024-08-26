import unittest
from unittest.mock import patch, Mock
from main.currency_exchanger import CurrencyExchanger


class TestCurrencyExchanger(unittest.TestCase):
    @patch('requests.get')
    def test_currency_exchange_thb_to_krw(self, mock_get):
        # Mock response from the API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'base': 'THB',
            'result': {'KRW': 38.69}
        }
        
        mock_get.return_value = mock_response

        exchanger = CurrencyExchanger(base_currency="THB", target_currency="KRW")
        
        amount = 100
        exchanged_amount = exchanger.currency_exchange(amount)
    
        expected_amount = amount * 38.69

        print("Expected Amount = ",expected_amount)
        print("Exchanged Amount = ", exchanged_amount)

        self.assertEqual(exchanged_amount, expected_amount)
        mock_get.assert_called_once_with(exchanger.currency_api, params={'from': 'THB', 'to': 'KRW'})

if __name__ == '__main__':
    unittest.main()
