import unittest
from unittest.mock import patch
from apps.shop_app.rapidapi.receive_data import get_sneakers
from .data import sneakers_data


class TestGetSneakers(unittest.TestCase):
    @patch("requests.request")
    def test_get_sneakers_success(self, mock_request):
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = sneakers_data
        response = get_sneakers()
        self.assertEqual(response, sneakers_data)
        self.assertEqual(
            response["results"][0]["name"], "Test KD 3 Retro Christmas (2023)"
        )
        self.assertEqual(response["results"][0]["brand"], "Test Brand")
        self.assertEqual(
            response["results"][0]["colorway"], "Test Yellow/Photo Test-Team Orange"
        )
        self.assertEqual(
            response["results"][0]["id"], "testtest-test-test-test-testtesttest"
        )
        self.assertEqual(response["results"][0]["retailPrice"], 130)
        self.assertEqual(
            response["results"][0]["story"], "this is sneakers description"
        )
        mock_request.assert_called_once()

    @patch("requests.request")
    def test_get_sneakers_failure(self, mock_request):
        # Mock failed API response
        mock_request.return_value.status_code = 400
        mock_request.return_value.json.return_value = {"error": "Bad request"}

        response = get_sneakers()

        self.assertEqual(response, {"error": "Bad request"})
        mock_request.assert_called_once()
