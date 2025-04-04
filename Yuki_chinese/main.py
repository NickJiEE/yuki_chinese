import uvicorn
import os
from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI()
    
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Index page
@app.get("/", response_class=HTMLResponse)
async def girl_one(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/girls")
async def girls_page(request: Request):
    return templates.TemplateResponse("girls.html", {"request": request})

@app.get("/services", response_class=HTMLResponse)
async def girl_one(request: Request):
    return templates.TemplateResponse("services.html", {"request": request})

@app.get("/price", response_class=HTMLResponse)
async def girl_one(request: Request):
    return templates.TemplateResponse("price.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def girl_one(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/events", response_class=HTMLResponse)
async def girl_one(request: Request):
    return templates.TemplateResponse("events.html", {"request": request})

@app.get("/jobs", response_class=HTMLResponse)
async def girl_one(request: Request):
    return templates.TemplateResponse("jobs.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def girl_one(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/terms-and-conditions", response_class=HTMLResponse)
async def girl_one(request: Request):
    return templates.TemplateResponse("terms-and-conditions.html", {"request": request})

@app.get("/privacy", response_class=HTMLResponse)
async def girl_one(request: Request):
    return templates.TemplateResponse("privacy.html", {"request": request})

@app.get("/girl_one", response_class=HTMLResponse)
async def girl_one(request: Request):
    return templates.TemplateResponse("girl_one.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=6543, reload=True)