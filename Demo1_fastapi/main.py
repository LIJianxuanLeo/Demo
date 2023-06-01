from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()


class ItemsName(BaseModel):
    id: int
    name: str
    favorites: list


@app.post("/items/")
async def create_item(item: ItemsName) -> ItemsName:
    return item


@app.get("/items/")
async def read_items() -> list[ItemsName]:
    return [ItemsName(id=1, name="demo", favorites=[1, 2, 3])]
