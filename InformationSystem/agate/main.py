from Class import Client
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def main():
  return "OK"

@app.get("/client")
async def get_all_client():
  result = Client.get_all_client()
  return result

@app.post("/client/add")
async def add_client(req:Client.Client):
  new_clinet = Client.Client(staff_id=req.staff_id,
                             name=req.name,
                             tel_number=req.tel_number)
  Client.add_client(new_clinet)
  return "OK"

@app.get("/client/{id}")
async def get_client(id: int):
  result = Client.get_client(id)
  return result

@app.get("/test")
async def generate_test_data():
  Client.add_client(Client.Client(staff_id=1, name="오리온", tel_number="010-0000"))
  Client.add_client(Client.Client(staff_id=1, name="삼성", tel_number="010-0000"))
  Client.add_client(Client.Client(staff_id=1, name="LG", tel_number="010-0000"))
  Client.add_client(Client.Client(staff_id=2, name="롯데", tel_number="010-0000"))
  Client.add_client(Client.Client(staff_id=2, name="코카콜라", tel_number="010-0000"))
  Client.add_client(Client.Client(staff_id=2, name="카시오", tel_number="010-0000"))
  Client.add_client(Client.Client(staff_id=3, name="Apple", tel_number="010-0000"))
  Client.add_client(Client.Client(staff_id=4, name="수원시청", tel_number="010-0000"))

  return "OK"

uvicorn.run(app, host="0.0.0.0", port="8000")