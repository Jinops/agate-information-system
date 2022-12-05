from pydantic import BaseModel
from typing import Union
from . import utils

class Advert(BaseModel):
  id: Union[int, None]
  campaign_id: int = None
  title: str
  content: str
  progress: str
  start_date: str
  end_date: str = utils.get_day_after(7)

db = []

def add(campaign_id, title, content, progress, start_date, end_date):
  dict = {
    "id": utils.get_new_id(db),
    "campaign_id": campaign_id,
    "title": title,
    "content": content,
    "progress": progress,
    "start_date": start_date,
    "end_date": end_date,
  }
  db.append(dict)
  return dict

def get(id: int):
  return utils.search(db, 'id', id)

def get_all():
  return db

def get_list_by_campaign(campaign_id: int):
  return utils.searches(db, 'campaign_id', campaign_id)

def update(id, update_data):
  return utils.update(db, id, update_data)
