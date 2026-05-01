from fastapi import FastAPI
from fastapi import APIRouter

app=FastAPI()
router=APIRouter()

@router.get("/")
def read_root():
    return {"status": "online", "message": "Hello from CI/CD"}

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "active": True} 

app.include_router(router)