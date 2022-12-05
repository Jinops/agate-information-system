from fastapi import FastAPI
import uvicorn

from Class import Client
from Class import Campaign
from Class import Advert

tags_metadata = [ 
  {
    "name": "clients",
    "description": "Agate의 고객",
  },
  {
    "name": "campaigns",
    "description": "광고 활동의 집합",
  },
  {
    "name": "adverts",
    "description": "개별 광고",
  },
] # https://ie.jinwoop.repl.co/docs
app = FastAPI(openapi_tags=tags_metadata)


@app.get("/")
async def main():
  return "OK"


## client


@app.get("/clients", tags=["clients"])
async def get_all_client():
  res = Client.get_all()
  return res


@app.get("/clients/{id}", tags=["clients"])
async def get_client(id: int):
  res = Client.get(id)
  return res


@app.post("/clients/add", tags=["clients"])
async def add_client(req: Client.Client, ):
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


@app.get("/campaigns", tags=["campaigns"])
async def get_all_campaign():
  res = Campaign.get_all()
  return res


@app.get("/campaigns/{id}", tags=["campaigns"])
async def get_campaign(id: int):
  res = Campaign.get(id)
  return res


@app.get("/campaigns/by_client/{client_id}", tags=["campaigns"])
async def get_campaign_by_client(client_id: int):
  res = Campaign.get_list_by_client(client_id)
  return res


@app.post("/campaigns/add", tags=["campaigns"])
async def add_campaign(req: Campaign.Campaign):
  Campaign.add(req.client_id, req.title, req.advert_id_list, req.start_date,
               req.end_date)
  return "OK"


## advert

@app.get("/adverts", tag=["adverts"])
async def get_all_advert():
  res = Advert.get_all()
  return res

@app.get("/adverts/{id}", tag=["adverts"])
async def get_advert(id: int):
  res = Advert.get(id)
  return res
  
@app.put("/adverts/{id}", tag=["adverts"])
async def get_advert():
  res = Advert.get()
  return res

@app.get("/adverts/by_campaign/{campaign_id}", tag=["adverts"])
async def get_advert_by_campaign(campaign_id: int):
  res = Advert.get_list_by_campaign(campaign_id)
  return res


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

  Campaign.add(client_id=1,
               title="고전 캠페인",
               advert_id_list=[],
               start_date="2019-01-01",
               end_date="2019-12-31")
  Campaign.add(client_id=2,
               title="상반기 캠페인",
               advert_id_list=[],
               start_date="2022-01-01",
               end_date="2022-05-31")
  Campaign.add(client_id=2, title="12월 연휴 캠페인", advert_id_list=[])

  return "OK"


uvicorn.run(app, host="0.0.0.0", port="8000")
