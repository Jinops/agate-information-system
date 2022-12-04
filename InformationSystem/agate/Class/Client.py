from pydantic import BaseModel
from typing import Optional
from . import utils


class Client(BaseModel):
  id: Optional[int] = None
  staff_id: int
  name: str
  tel_number: str

db = []  # dictionary list


def add_client(client: Client):
  client.id = utils.get_new_id(db)
  db.append(dict)


def get_client(id: int):
  return utils.search(db, 'id', id)


def get_all_client():
  return db
