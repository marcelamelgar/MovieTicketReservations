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
    time: str
    topay: float

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def cartelera(request: Request):
    return templates.TemplateResponse("cartelera.html", {"request": request})

@app.get("/hora/{chosen_movie}", response_class=HTMLResponse)
async def read_movie(request: Request, chosen_movie: str):
    horas = []
    if chosen_movie == 'brujas':
        movie = 'Cacería de Brujas'
        horas = [['10:15'],['13:05'],['15:45'],['16:22'],['18:30']]
    elif chosen_movie == 'casate':
        movie = 'Cásate Conmigo'
        horas = [['11:20'],['14:05'],['17:45']]
    elif chosen_movie == 'corazon':
        movie = 'Corazón de Fuego'
        horas = [['14:00'],['19:00']]
    elif chosen_movie == 'padrino':
        movie = 'El Padrino 50 años'
        horas = [['16:00'],['20:30'],['21:05']]
    elif chosen_movie == 'banishing':
        movie = 'El Exorcismo'
        horas = [['18:35'],['20:45'],['22:15'],['23:55']]
    elif chosen_movie == 'sing':
        movie = 'Sing 2: ¡Ven y Canta de Nuevo!'
        horas = [['16:20'],['17:30'],['21:15']]
    return templates.TemplateResponse("hora.html",{"request": request, "chosen_movie": chosen_movie, "movie":movie, "horas":horas})

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