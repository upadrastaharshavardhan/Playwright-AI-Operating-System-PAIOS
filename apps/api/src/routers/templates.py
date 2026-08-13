from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_templates():
    return [
        {"id": "tpl-login", "name": "Login Template", "module": "Auth", "status": "active"},
        {"id": "tpl-search", "name": "Search Template", "module": "Search", "status": "active"},
        {"id": "tpl-checkout", "name": "Checkout Template", "module": "Checkout", "status": "active"},
    ]
