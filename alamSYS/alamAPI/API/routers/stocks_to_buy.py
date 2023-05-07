from fastapi import APIRouter
from DB_model.models import Buy
from datetime import datetime
from json import loads


router = APIRouter(
    prefix="/stocks_to_buy",
    tags=["Stocks to Buy"],
)


# ====== STOCKS TO BUY ==================================================
# Get all stocks to buy
# This is a public endpoint and does not require authentication
@router.get("/all")
def get_all_stocks_to_buy():
    # Get all data from the "Buy" collection
        data = Buy.objects().to_json()
        json_data = loads(data)
        # Return the data and the current datetime
        return {
                "Stocks": json_data,
                "DateTime": datetime.now()
        }


# Get a specific stock to buy
# This is a public endpoint and does not require authentication
@router.get("/{stock_code}")
def get_stock_to_buy(stock_code: str):
        stock_code_query = stock_code.upper()
        # Get stock info from the "Buy" collection
        data = Buy.objects(stock_symbol=stock_code_query).to_json()
        json_data = loads(data)
        # Return the data and the current datetime
        return {
                "Stock": json_data if json_data else "Stock not found",
                "DateTime": datetime.now()
        }
# ====== END STOCKS TO BUY ==============================================
