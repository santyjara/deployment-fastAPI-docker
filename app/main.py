from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load('model.joblib')


class Item(BaseModel):
    feature_1: int
    feature_2: int


@app.post("/")
async def create_item(item: Item):

    pred = model.predict([[item.feature_1, item.feature_2]])[0]

    return {'prediction': int(pred)}
