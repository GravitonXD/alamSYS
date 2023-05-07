from mongoengine import Document, StringField, FloatField, ListField, IntField, DictField


"""
About the Buy class:
    - This class is used to define the structure of the "buy" collection in the MongoDB database
    - This document contains the stocks to buy based from the predicted price trend from the Machine Learning model
"""
class Buy(Document):
    stock_symbol =  StringField()
    last_closing =  FloatField()
    last_date = StringField()
    predicted_closing = DictField()

    def to_json(self):
        return {
            "stock_symbol": self.stock_symbol,
            "last_closing": self.last_closing,
            "last_date": self.last_date,
            "predicted_closing": self.predicted_closing
        }


""""
About the Sell class:
    - This class is used to define the structure of the "sell" collection in the MongoDB database
    - This document contains the stocks to sell based from the predicted price trend from the Machine Learning model
"""
class Sell(Document):
    stock_symbol =  StringField()
    last_closing =  FloatField()
    last_date = StringField()
    predicted_closing = DictField()

    def to_json(self):
        return {
            "stock_symbol": self.stock_symbol,
            "last_closing": self.last_closing,
            "last_date": self.last_date,
            "predicted_closing": self.predicted_closing
        }
    

"""
About the Info class:
    - This class is used to define the structure of the "info" collection in the MongoDB database
    - This document contains the general information of the stocks included in the alamSYS
"""
class Info(Document):
    stock_symbol =  StringField()
    stock_name = StringField()
    company_site = StringField()
    company_address = StringField()
    company_email = StringField()
    company_phone = IntField()
    sector = StringField()
    industry = StringField()
    key_executives = ListField()
    
    def to_json(self):
        return {
            "stock_symbol": self.stock_symbol,
            "stock_name": self.stock_name,
            "company_site": self.company_site,
            "company_address": self.company_address,
            "company_email": self.company_email,
            "company_phone": self.company_phone,
            "sector": self.sector,
            "industry": self.industry,
            "key_executives": self.key_executives
        }


"""
About the MlModelsInfo class:
    - This class is used to define the structure of the "mlModelsInfo" collection in the MongoDB database
    - This document contains the information of the Machine Learning models used in the alamSYS
"""
class MlModelsInfo(Document):
    model_name = StringField()
    model_description = StringField()
    model_scores = DictField()

    def to_json(self):
        return {
            "model_name": self.model_name,
            "model_description": self.model_description,
            "model_scores": self.model_scores
        }
    

"""
About the StockRisksProfile class:
    - This class is used to define the structure of the "stockRisksProfile" collection in the MongoDB database
    - This document contains the information of the risks of the stocks included in the alamSYS
"""
class StockRisksProfile(Document):
    stock_symbol = StringField()
    value_at_risk = FloatField()
    volatility = FloatField()
    drawdown = FloatField()
    start_date = StringField()
    end_date = StringField()

    def to_json(self):
        return {
            "stock_symbol": self.stock_symbol,
            "value_at_risk": self.value_at_risk,
            "volatility": self.volatility,
            "drawdown": self.drawdown,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
    