from bson import ObjectId
from celery import group
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from starlette.responses import JSONResponse
from celery_tasks.tasks import *
from schemas.schemas import CreateChat
router = APIRouter(prefix='/chat', tags=['chat'], responses={404: {"description": "Error Occured"}})

@router.get("/")
async def chatGetDetails() -> dict:
    data = GetAllChat.apply_async()
    data = data.get()
    data = json.loads(data)
    return JSONResponse(data)

@router.get("/{id}")
async def chatGetDetailsbySessionId(id:str) -> dict:
    data = GetChatBySessionId.apply_async(args=[id])
    data = data.get()
    data = json.loads(data)
    return JSONResponse(data)

@router.post("/create")
async def chatCreateDetails(request: Request):
    """
    Post API data for to create user data
    """
    data = await request.json()
    savingChat.apply_async(args=[data])
    return JSONResponse({"message": "Chat Data Recieved"})

@router.put("/update")
async def chatUpdateDetails(request: Request):
    """
    Put API data for to update user data
    """
    data = await request.json()
    updateUser.apply_async(args=[data])
    return JSONResponse({"message": "Updated User Data"})


@router.delete("/delete")
async def chatDeleteDetails(request: Request):
    """
    API data for to delte user data
    """
    data = await request.json()
    deleteUser.apply_async(args=[data])
    return JSONResponse({"message": "Deleted User Data"})




