from pydantic import BaseModel
from typing import List, Optional
from . import utils


class Campaign(BaseModel):
  id: Optional[int] = None
  client_id: int
  title: str
  advert_id_list: List[int]
  start_date: Optional[str]
  end_date: Optional[str]


db = []


def add(client_id, title, advert_id_list, start_date, end_date):
  if start_date is None and end_date is None:
    start_date = utils.get_today()
    end_date = utils.get_day_after(7)

  dict = {
    "id": utils.get_new_id(db),
    "client_id": client_id,
    "title": title,
    "advert_id_list": advert_id_list,
    "start_date": start_date,
    "end_date": end_date,
  }
  db.append(dict)


def get(id: int):
  return utils.search(db, 'id', id)


def get_list_by_client(client_id: int):
  return utils.searches(db, 'client_id', client_id)


def get_all():
  return db
