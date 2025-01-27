from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.post("/api/ai/checklist")
async def checklist(project_code:str):
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
