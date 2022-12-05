from pydantic import BaseModel
from typing import List, Union
from . import utils


class Campaign(BaseModel):
  id: Union[int, None]
  client_id: int = None
  title: str = ""
  advert_id_list: List[int] = []
  start_date: str = utils.get_today()
  end_date: str = utils.get_day_after(7)


db = []


def add(client_id, title, advert_id_list, start_date=None, end_date=None):
  dict = {
    "id": utils.get_new_id(db),
    "client_id": client_id,
    "title": title,
    "advert_id_list": advert_id_list,
    "start_date": start_date,
    "end_date": end_date,
  }
  db.append(dict)
  return dict


def get(id: int):
  return utils.search(db, 'id', id)


def get_list_by_client(client_id: int):
  return utils.searches(db, 'client_id', client_id)


def get_all():
  return db
