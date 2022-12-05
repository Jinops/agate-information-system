from pydantic import BaseModel
from typing import Optional
from . import utils

class Advert:
  id: Optional[int] = None
  campaign_id: int
  title: str
  content: str
  progress: str
  start_date: Optional[str]
  end_date: Optional[str]

db = []

def add(campaign_id, title, content, progress, start_date = None, end_date = None):
  if start_date is None and end_date is None:
    start_date = utils.get_today()
    end_date = utils.get_day_after(7)
    
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

def get(id: int):
  return utils.search(db, 'id', id)

def get_all():
  return db

def get_list_by_campaign(campaign_id: int):
  return utils.searches(db, 'campaign_id', campaign_id)

def update(id, update_data):
  utils.update(db, id, update_data)
