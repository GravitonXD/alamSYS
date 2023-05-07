# Python Imports
from fastapi import FastAPI
from mongoengine import connect
from os import environ
# Import routers
from routers import home, stocks_to_buy, stocks_to_sell, stocks_info, ml_model_info, stock_risks_profile


# Create the FastAPI app
app = FastAPI(
        title="alamAPI",
        description="alamAPI is an API for the alamSYS, a Philippine Stock Market Price Trend Forecasting System \nThis project is part of the requirements for the completion of BS Computer Science at the University of the Philippines Visayas \nDeveloped solely by: John Markton M. Olarte",
        version="1.0.0",
        docs_url="/alamAPI/v1/docs",
        openapi_url="/alamAPI/v1/openapi.json",
        redoc_url="/alamAPI/v1/redoc",
        contact={
                "name": "John Markton M. Olarte",
                "email": "jmolarte@up,edu.ph"
        },
        openapi_tags=[
                {
                        "name": "Home",
                        "description": "This API endpoint outputs a welcome message. Which should inform the user that they have successfully connected to the alamAPI."
                },
                {
                        "name": "Stocks to Buy",
                        "description": "This API endpoint outputs a list of suggested stocks to buy based from the current market price and the predicted price up-trend."
                },
                {
                        "name": "Stocks to Sell",
                        "description": "This API endpoint outputs a list of suggested stocks to sell based from the current market price and the predicted price down-trend."
                },
                {
                        "name": "Stocks Info",
                        "description": "This API endpoint outputs a list of stocks included in the alamSYS and their corresponding information."
                },
                {
                        "name": "ML Model Info",
                        "description": "This API endpoint outputs a list of the Machine Learning Models used in the alamSYS and their corresponding information."
                },
                {
                        "name": "Stocks Risks Profile",
                        "description": "This API endpoint outputs a list of the stocks included in the alamSYS and their corresponding risks values based on value at risk (%), volatility (%), and drawdown (%)."
                }
        ]
)


# Connect to the database, using the environment variables (set in the docker-compose.yml file)
connect(db=environ['MONGO_INITDB_DATABASE'], host=environ['MONGO_HOST'], port=int(environ['MONGO_PORT']))


# HOME
app.include_router(home.router)
# STOCKS TO BUY
app.include_router(stocks_to_buy.router)
# STOCKS TO SELL
app.include_router(stocks_to_sell.router)
# STOCKS INFO
app.include_router(stocks_info.router)
# ML MODEL INFO
app.include_router(ml_model_info.router)
# RISK INFO
app.include_router(stock_risks_profile.router)


if __name__ == "__main__":
    # Run the app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    