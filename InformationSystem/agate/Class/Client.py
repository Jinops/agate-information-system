from typing import Optional
from pydantic import BaseModel
from . import utils


class Client(BaseModel):
  id: Optional[int] = None
  staff_id: int
  name: str
  tel_number: str

db = []  # dictionary list


def add_client(client):
  client_dict = vars(client)
  client_dict['id'] = utils.get_new_id(db)
  db.append(client_dict)


def get_client(id: int):
  return utils.search(db, 'id', id)


def get_all_client():
  return db
