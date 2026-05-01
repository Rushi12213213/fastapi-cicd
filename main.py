from fastapi import FastAPI
from fastapi import APIRouter
import time

app=FastAPI()
router=APIRouter()

@router.get("/")
def read_root():
    return {"status": "online", "message": "Server is online"}

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "active": True} 

@router.get("/delay")
def read_item():
    time.sleep(2)
    return {"message":"server is healthy"} 

app.include_router(router)