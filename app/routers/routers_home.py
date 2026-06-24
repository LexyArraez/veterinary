from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["Home"])
def home():
    return {"message": "Clínica veterinaria - FemCoders Madrid P5"}