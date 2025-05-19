from fastapi import APIRouter, File, UploadFile
from src.controller.upload_controller import run

uploadRoute = APIRouter()


@uploadRoute.post('/upload')
async def upload(file:UploadFile = File(...)):
     return await run(file)

