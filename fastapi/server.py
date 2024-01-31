from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List
from compas.geometry import oriented_bounding_box

app = FastAPI()


class OrientedBoundingBoxInput(BaseModel):
    points: List[List[float]]


@app.get("/")
async def root():
    return "Hello, this is a simple COMPAS server."


@app.post("/oriented_bounding_box")
async def obb(oriented_bounding_box_input: OrientedBoundingBoxInput):
    return oriented_bounding_box(oriented_bounding_box_input.points)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
