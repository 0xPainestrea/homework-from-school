from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/history", response_class=HTMLResponse)
async def history(request: Request):
    return templates.TemplateResponse("newhistory.html", {"request": request})

@app.get("/creative", response_class=HTMLResponse)
async def creative(request: Request):
    return templates.TemplateResponse("creative.html", {"request": request})

@app.get("/academic", response_class=HTMLResponse)
async def academic(request: Request):
    return templates.TemplateResponse("academic.html", {"request": request})


@app.get("/experince", response_class=HTMLResponse)
async def experince(request: Request):
    return templates.TemplateResponse("experince.html", {"request": request})

@app.get("/photo", response_class=HTMLResponse)
async def photo(request: Request):
    return templates.TemplateResponse("photo.html", {"request": request})