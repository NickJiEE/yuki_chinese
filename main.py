import uvicorn
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI()
    
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Index page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/girl-list")
async def girls_page(request: Request):
    return templates.TemplateResponse("girl-list.html", {"request": request})

@app.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    return templates.TemplateResponse("services.html", {"request": request})

@app.get("/price", response_class=HTMLResponse)
async def price(request: Request):
    return templates.TemplateResponse("price.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/events", response_class=HTMLResponse)
async def events(request: Request):
    return templates.TemplateResponse("events.html", {"request": request})

@app.get("/jobs", response_class=HTMLResponse)
async def jobs(request: Request):
    return templates.TemplateResponse("jobs.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/terms-and-conditions", response_class=HTMLResponse)
async def terms_and_conditions(request: Request):
    return templates.TemplateResponse("terms-and-conditions.html", {"request": request})

@app.get("/privacy", response_class=HTMLResponse)
async def privacy(request: Request):
    return templates.TemplateResponse("privacy.html", {"request": request})

# Girls pages
@app.get("/girls/dingdangmao", response_class=HTMLResponse)
async def dingdangmao(request: Request):
    return templates.TemplateResponse("girls/dingdangmao.html", {"request": request})

@app.get("/girls/kuikui", response_class=HTMLResponse)
async def kuikui(request: Request):
    return templates.TemplateResponse("girls/kuikui.html", {"request": request})

@app.get("/girls/miemie", response_class=HTMLResponse)
async def miemie(request: Request):
    return templates.TemplateResponse("girls/miemie.html", {"request": request})

@app.get("/girls/xiaowu", response_class=HTMLResponse)
async def xiaowu(request: Request):
    return templates.TemplateResponse("girls/xiaowu.html", {"request": request})

@app.get("/girls/youyou", response_class=HTMLResponse)
async def youyou(request: Request):
    return templates.TemplateResponse("girls/youyou.html", {"request": request})

@app.get("/girls/youzi", response_class=HTMLResponse)
async def youzi(request: Request):
    return templates.TemplateResponse("girls/youzi.html", {"request": request})

@app.get("/girls/xiaoyang", response_class=HTMLResponse)
async def xiaoyang(request: Request):
    return templates.TemplateResponse("girls/xiaoyang.html", {"request": request})

@app.get("/girls/ningmeng", response_class=HTMLResponse)
async def ningmeng(request: Request):
    return templates.TemplateResponse("girls/ningmeng.html", {"request": request})

@app.get("/favicon.ico")
def favicon():
    file_path = os.path.join("static", "icons", "favicon.ico")
    return FileResponse(file_path)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    