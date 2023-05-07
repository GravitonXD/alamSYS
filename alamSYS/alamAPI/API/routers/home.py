from fastapi import APIRouter

router = APIRouter(
    prefix="/home",
    tags=["Home"],
)


# ====== HOME ==================================================
@router.get("/")
def home():
    message = " Welcome to alamAPI an API for the alamSYS a Philippine Stock Market Price Trend Forecasting System, developed by John Markton M. Olarte as a partial requirement for the degree of Bachelor of Science in Computer Science at the University of the Philippines - Visayas."
    return {"message": message}
# ====== END HOME ==============================================
