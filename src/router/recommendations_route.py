from fastapi import APIRouter
from src.controller.recommendations_controller import run

recommendationsRoute = APIRouter()

@recommendationsRoute.get('/recommendations')
async def recommendations():
     await run()