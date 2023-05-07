from fastapi import APIRouter
from DB_model.models import StockRisksProfile
from datetime import datetime
from json import loads


router = APIRouter(
    prefix="/risk_info",
    tags=["Stock Risks Profile"],
)


# ===== STOCKS RISKS PROFILE =====================================================
# Get all stocks Risk Profile
# This is a public endpoint and does not require authentication
@router.get("/all", tags=["Stock Risks Profile"])
def get_all_stocks_stocks_risks_profile():
        data = StockRisksProfile.objects().to_json()
        json_data = loads(data)
        # Return the data and the current datetime
        return {
                "All Stocks Risks Profile": json_data,
                "Date and Time": datetime.now()
        }


# Get a specific stock Risk Profile
# This is a public endpoint and does not require authentication
@router.get("/{stock_code}", tags=["Stock Risks Profile"])
def get_stock_stocks_risks_profile(stock_code: str):
        stock_code_query = stock_code.upper()
        # Get stock StockRisksProfile from the "StockRisksProfile" collection
        data = StockRisksProfile.objects(stock_symbol=stock_code_query).to_json()
        json_data = loads(data)
        # Return the data and the current datetime
        return {
                "Stock Risks Profile": json_data if json_data else "Stock not found",
                "Date and Time": datetime.now()
        }
# ===== END STOCKS StockRisksProfile =================================================
