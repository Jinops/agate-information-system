from Class import Client

Client.add_client(Client.Client(1, "테스트", ""))
Client.add_client(Client.Client(1, "테스트2", ""))
Client.add_client(Client.Client(1, "테스트3", ""))

print(Client.get_all_client())
print(Client.get_client(2))

c = Client.Client(1, "테4", "")
Client.add_client(c)
print(Client.get_all_client())

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse
from enum import Enum
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/client")
async def get_all_client():
  result = Client.get_all_client()
  return {}

@app.post("/client/add")
async def add_client(req):
  new_clinet = Client.Client(staff_id=req.staff_id,
                             name=req.name,
                             tel_number=req.tel_number)
  Client.add_client(new_clinet)
  return {}


@app.get("/client/{id}")
async def get_client(id: int):
  result = Client.get_client(id)
  return {}

uvicorn.run(app, host="0.0.0.0", port="8000")