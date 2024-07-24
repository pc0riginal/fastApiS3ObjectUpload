from fastapi import FastAPI, Request, Form , UploadFile,File,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from upload_to_s3.upload import upload

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def get_form():
    return "hello world"

@app.get('/form')
async def get_form(request: Request):
    result = "upload a file"
    return templates.TemplateResponse("index.html", context={"request": request,"result":result})

@app.post('/uploadfile/')
async def upload_file(request: Request,file: UploadFile = File(...)):
    try:
        res = upload(file)
        return templates.TemplateResponse("index.html", context={"request": request, "result": res})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")
    finally:
        file.file.close()

