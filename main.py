import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import database

app = FastAPI()

class mk(BaseModel):
    mid: str
    info: str
    char: str

class mid(BaseModel):
    mid: str

@app.post("/mk_info")
async def create(response: mk):
    database.cre(dict(response))

@app.put("/mk_info")
async def change(response: mk):
    database.put(dict(response))

@app.post("/mk_info_d")
async def delete(response: mid):
    database.delete(dict(response))

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)