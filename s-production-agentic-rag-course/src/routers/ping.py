from fastapi import APIRouter

router = APIRouter()
@router.get("/ping", tags=["Health"])
async def ping():
    """Simple ping endpoint for basic connectivity tests."""
    return {"status": "ok", "message": "pong Srinivas"}