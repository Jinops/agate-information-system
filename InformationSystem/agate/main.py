from fastapi import FastAPI
import uvicorn

from Class import Client
from Class import Campaign

app = FastAPI()


@app.get("/")
async def main():
  return "OK"


## client

@app.get("/clients")
async def get_all_client():
  res = Client.get_all()
  return res


@app.get("/clients/{id}")
async def get_client(id: int):
  res = Client.get(id)
  return res
  
@app.post("/clients/add")
async def add_client(req: Client.Client):
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

@app.get("/campaigns")
async def get_all_campaign():
  res = Campaign.get_all()
  return res

@app.get("/campaigns/{id}")
async def get_campaign(id: int):
  res = Campaign.get(id)
  return res

@app.get("/campaigns/by_client/{client_id}")
async def get_campaign_by_client(client_id: int):
  res = Campaign.get_list_by_client(client_id)
  return res

@app.post("/campaigns/add")
async def add_campaign(req: Campaign.Campaign):
  Campaign.add(req.client_id, req.title, req.advert_id_list, req.start_date, req.end_date)
  return "OK"
'''
{
    "client_id": 1,
    "title": "하반기 캠페인",
    "advert_id_list": [1,2]
 }
'''

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

  Campaign.add(client_id=1, title="고전 캠페인", advert_id_list=[], start_date="2019-01-01", end_date="2019-12-31")
  Campaign.add(client_id=2, title="상반기 캠페인", advert_id_list=[], start_date="2022-01-01", end_date="2022-05-31")
  Campaign.add(client_id=2, title="12월 연휴 캠페인", advert_id_list=[])

  return "OK"


uvicorn.run(app, host="0.0.0.0", port="8000")
