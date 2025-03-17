from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from app.models.model_reverse_ip import ReverseIPSchema
from app.services.service_reverse_ip import ReverseIPService

router = APIRouter(
    prefix="/reverse_ip",
    tags=["REVERSE IP"],
    responses={404: {"message": "Not found"}}
)

reverseip_service = ReverseIPService()

@router.post("/get_lookup")
async def get_lookup(data: ReverseIPSchema = Depends(ReverseIPSchema)):
    return reverseip_service.get_lookup(data.ip_address)