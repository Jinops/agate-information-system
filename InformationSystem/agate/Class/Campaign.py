from pydantic import BaseModel
from typing import Optional
from . import utils


class Campaign:
    id: Optional[int] = None
    client_id: int
    title: str
    advert_id_list: list[int]
    start_date: str = utils.get_today()
    end_date: str = utils.get_day_after(7)


db = []

def add_campaign(campaign:Campaign):
  campaign.id = utils.get_new_id(db)
  db.append(campaign)


def get_campaign(id: int):
  return utils.search(db, 'id', id)


def get_all_campaign():
  return db
