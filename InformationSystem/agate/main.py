from fastapi import FastAPI
import uvicorn

from Class import Client
from Class import Campaign

app = FastAPI()

@app.get("/")
async def main():
  return "OK"

## client

@app.get("/client")
async def get_all_client():
  res = Client.get_all()
  return res

@app.get("/client/{id}")
async def get_client(id: int):
  res = Client.get(id)
  return res

@app.post("/client/add")
async def add_client(req:Client.Client):
  Client.add(req.staff_id, req.name, req.tel_number)
  return {}
'''
{
  "staff_id":1,
  "name":"replit",
  "tel_number":"1234"
}
'''

## campaign

@app.get("/campaign")
async def get_all_client():
  res = Campaign.get_all()
  return res

@app.get("/campaign/{id}")
async def get_campaign(id: int):
  result = Campaign.get(id)
  return result

@app.post("/campaign/add")
async def add_campaign(req:Campaign.Campaign):
  Campaign.add(req.client_id, req.title, req.advert_id_list, req.start_date, req.end_date)
  return "OK"
  
## test

@app.get("/test")
async def generate_test_data():
  Client.add(staff_id=1, name="오리온", tel_number="010-0000")
  Client.add(staff_id=1, name="삼성", tel_number="010-0000")
  Client.add(staff_id=1, name="LG", tel_number="010-0000")
  Client.add(staff_id=2, name="롯데", tel_number="010-0000")
  Client.add(staff_id=2, name="코카콜라", tel_number="010-0000")
  Client.add(staff_id=2, name="카시오", tel_number="010-0000")
  Client.add(staff_id=3, name="Apple", tel_number="010-0000")
  Client.add(staff_id=4, name="수원시청", tel_number="010-0000")

  return "OK"

uvicorn.run(app, host="0.0.0.0", port="8000")