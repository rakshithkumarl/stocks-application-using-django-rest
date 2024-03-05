# Django REST Stock Application

This Django REST application serves as a stock management system, providing APIs to interact with stock data. It utilizes Django Rest Framework for building APIs to manage the stocks.

## Features

- **APIs for Stock Management**: This application offers the following APIs:
  - `/list-stocks/`: Returns a list of all available stocks.
  - `/list-stocks-by-status/`: Returns a list of stocks filtered by the specified status (e.g., "In Stock", "Out of Stock", "Low Stock").
  - `/list-stocks-by-date-range/`: Returns a list of stocks filtered by the specified date range.

- **Data Modelling**: The application has a `Stocks` data-model and it uses the SQLite3 database for data storage and retrieval.

- **Token-based Authentication**: Authentication is implemented using token-based authentication, providing secure access to the APIs. Only users with valid tokens can access the endpoints.

- **Unit Tests**: Unit tests are added to validate the functionality of each API endpoint, ensuring proper handling of requests and responses.

# API Specification

## List Stocks Endpoint

- **URL**: `/list-stocks/`
- **HTTP Method**: GET
- **Authentication**: Token authentication required
- **Permissions**: Only admin users can access this view
- **Description**: Returns a list of all stocks available.

### Response:
- **Status Code**: 200 OK
- **Content Type**: application/json

```json
[
    {
        "sku": "ABC123",
        "name": "Product Name 1",
        "category": "Category 1",
        "tags": ["Tag1", "Tag2"],
        "stock_status": "In Stock",
        "available_stock": 100
    },
    {
        "sku": "XYZ456",
        "name": "Product Name 2",
        "category": "Category 2",
        "tags": ["Tag3", "Tag4"],
        "stock_status": "Out of Stock",
        "available_stock": 0
    },
]
```

## List Stocks by Status Endpoint

- **URL:** `/list-stocks-by-status/?stock_status={status}`
- **HTTP Method:** GET
- **Authentication:** Token authentication required
- **Permissions:** Only admin users can access this view

### Description:
Returns a list of stocks filtered by the specified status.

### Query Parameters:
- `stock_status` (required): The status of stocks to filter by. Possible values: "In Stock", "Out of Stock", "Low Stock", etc.

### Response:
- **Status Code:** 200 OK
- **Content Type:** application/json

```json
[
    {
        "sku": "ABC123",
        "name": "Product Name 1",
        "category": "Category 1",
        "stock_status": "In Stock",
        "available_stock": 100
    },
    {
        "sku": "XYZ456",
        "name": "Product Name 2",
        "category": "Category 2",
        "stock_status": "In Stock",
        "available_stock": 50
    },
    
]
```

## List Stocks by Date Range Endpoint

- **URL**: `/list-stocks-by-date-range/?start_date={start_date}&end_date={end_date}`
- **HTTP Method**: GET
- **Authentication**: Token authentication required
- **Permissions**: Only admin users can access this view

### Description:
Returns a list of stocks filtered by the specified date range.

### Query Parameters:
- `start_date` (required): The start date of the date range in YYYY-MM-DD format.
- `end_date` (required): The end date of the date range in YYYY-MM-DD format.

### Response:
- **Status Code**: 200 OK
- **Content Type**: application/json

```json
[
    {
        "sku": "ABC123",
        "name": "Product Name 1",
        "category": "Category 1",
        "stock_status": "In Stock",
        "available_stock": 100
    },
    {
        "sku": "XYZ456",
        "name": "Product Name 2",
        "category": "Category 2",
        "stock_status": "Out of Stock",
        "available_stock": 0
    },

]

