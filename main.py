from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

class Item(BaseModel):
    name: str
    payment: str
    tickets: int
    movie: str
    time: datetime
    topay: float

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def cartelera(request: Request):
    return templates.TemplateResponse("cartelera.html", {"request": request})

@app.get("/hora/{chosen_movie}", response_class=HTMLResponse)
async def read_movie(request: Request, chosen_movie: str):
    return templates.TemplateResponse("hora.html",{"request": request, "chosen_movie": chosen_movie})

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}