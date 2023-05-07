from fastapi import APIRouter
from DB_model.models import MlModelsInfo as Info
from datetime import datetime
from json import loads


router = APIRouter(
    prefix="/ml_model_info",
    tags=["ML Model Info"],
)


# ===== ML MODEL INFO =====================================================
# Get all ML Model info
# This is a public endpoint and does not require authentication
@router.get("/all", tags=["ML Model Info"])
def get_all_models_info():
        # Get all data from the "Buy" collection
                data = Info.objects().to_json()
                json_data = loads(data)
                # Return the data and the current datetime
                return {
                        "All Models Info": json_data,
                        "Date and Time": datetime.now()
                }


# Get a specific ML Model info by model name
# This is a public endpoint and does not require authentication
@router.get("/{model_name}", tags=["ML Model Info"])
def get_model_info(model_name: str):
        model_code_query = model_name.upper()
        # Get model info from the "Info" collection
        data = Info.objects(model_name=model_code_query).to_json()
        json_data = loads(data)
        # Return the data and the current datetime
        return {
                # Return the model info, if the model code is not found, return "Model not found"
                "Model Info": json_data if json_data else "Model not found",
                "Date and Time": datetime.now()
        }
# ===== END ML MODEL INFO =================================================
