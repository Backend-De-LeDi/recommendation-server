from fastapi import UploadFile
from fastapi.responses import JSONResponse

async def run(file:UploadFile):
     if file.content_type not in ['application/psf',"application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
                  return JSONResponse(status_code=400,content={"msg": "Solo se permiten archivos PDF o DOCX"})
          
     content = await file.read()

     with open(f'./uploads/{file.filename}',"wb") as f:
                  f.write(content)

     path = f'./uploads/{file.filename}'

     return JSONResponse(status_code=200,content={"path":path })