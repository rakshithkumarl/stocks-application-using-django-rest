from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Stock

# Create your tests here.

class ListStocksTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_stocks_authenticated(self):
        # Authenticate the request (replace 'your_token' with a valid token)
        self.client.credentials(HTTP_AUTHORIZATION='Token your_token')
        response = self.client.get('/stocks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_stocks_unauthenticated(self):
        response = self.client.get('/stocks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class ListStocksByStatusTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_stocks_by_status_authenticated(self):
        # Authenticate the request (replace 'your_token' with a valid token)
        self.client.credentials(HTTP_AUTHORIZATION='Token your_token')
        response = self.client.get('stocks/list-stocks-by-status/?stock_status=In%20Stock')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_stocks_by_status_unauthenticated(self):
        response = self.client.get('stocks/list-stocks-by-status/?stock_status=In%20Stock')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class ListStocksByDateRangeTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_stocks_by_date_range_authenticated(self):
        # Authenticate the request (replace 'your_token' with a valid token)
        self.client.credentials(HTTP_AUTHORIZATION='Token your_token')
        response = self.client.get('stocks/list-stocks-by-date-range/?start_date=2024-02-01&end_date=2024-02-10')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_stocks_by_date_range_unauthenticated(self):
        response = self.client.get('stocks/list-stocks-by-date-range/?start_date=2024-02-01&end_date=2024-02-10')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

