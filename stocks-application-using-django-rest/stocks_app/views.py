from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import Stock
from .serializers import StockSerializer
from django.core.serializers import serialize
import json
from django.http import JsonResponse, HttpResponseForbidden


class ListStocks(APIView):
    """
    View to list all stocks.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all stocks.
        """
        stocks = Stock.objects.all().values('sku', 'name', 'category', 'tags', 'stock_status', 'available_stock')
        serialized_data = json.dumps(list(stocks), indent = 4)   
        parsed_data = json.loads(serialized_data) 
        return JsonResponse(parsed_data, safe=False)

class ListStocksByStatus(APIView):
    """
    View to list all stocks based by status.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all stocks by status.
        """
        stk_status = request.query_params.get('stock_status')
        stocks=Stock.objects.filter(stock_status = stk_status).values('sku', 'name', 'category', 'stock_status', 'available_stock')
        serialized_data = json.dumps(list(stocks), indent = 4)   
        parsed_data = json.loads(serialized_data) 
        return JsonResponse(parsed_data, safe=False)
    

class ListStocksByDateRange(APIView):
    """
    View to list all stocks by date range.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all stocks by date range.
        """
        token = "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
        _, token_url = request.headers.get("Auth").split(" ")
        print(token_url)
        if not token == token_url:
            return HttpResponseForbidden(f'Invalid Token')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        stocks = Stock.objects.filter(date__range=(start_date, end_date)).values('sku', 'name', 'category', 'tags', 'stock_status', 'available_stock')
        serialized_data = json.dumps(list(stocks), indent = 4)   
        parsed_data = json.loads(serialized_data) 
        return JsonResponse(parsed_data, safe=False)
