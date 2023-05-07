from fastapi import APIRouter
from DB_model.models import Sell
from datetime import datetime
from json import loads


router = APIRouter(
    prefix="/stocks_to_sell",
    tags=["Stocks to Sell"],
)


# ===== STOCKS TO SELL ==================================================
# get all stocks to sell
# This is a public endpoint and does not require authentication
@router.get("/all", tags=["Stocks to Sell"])
def get_all_stocks_to_sell():
    # Get all data from the "Buy" collection
        data = Sell.objects().to_json()
        json_data = loads(data)
        # Return the data and the current datetime
        return {
                "Stocks": json_data,
                "DateTime": datetime.now()
        }


# Get a specific stock to sell
# This is a public endpoint and does not require authentication
@router.get("/{stock_code}", tags=["Stocks to Sell"])
def get_stock_to_sell(stock_code: str):
        stock_code_query = stock_code.upper()
        # Get stock info from the "Buy" collection
        data = Sell.objects(stock_symbol=stock_code_query).to_json()
        json_data = loads(data)
        # Return the data and the current datetime
        return {
                "Stock": json_data if json_data else "Stock not found",
                "DateTime": datetime.now()
        }
# ===== END STOCKS TO SELL ===============================================
