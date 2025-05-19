from fastapi import FastAPI
from src.router.upload_route import uploadRoute
from src.router.recommendations_route import recommendationsRoute
import os

app = FastAPI()

uploadFolder = 'uploads'
if not os.path.exists(uploadFolder):
     os.makedirs(uploadFolder)

app.include_router(uploadRoute)
app.include_router(recommendationsRoute)