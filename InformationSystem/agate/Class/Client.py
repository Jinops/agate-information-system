from pydantic import BaseModel
from typing import Optional
from . import utils


class Client(BaseModel):
  id: Optional[int] = None
  staff_id: int
  name: str
  tel_number: str


db = []  # dictionary list

def add(staff_id, name, tel_number):
  dict = {
    "id": utils.get_new_id(db),
    "staff_id": staff_id,
    "name": name,
    "tel_number": tel_number,
  }
  db.append(dict)

def get(id: int):
  return utils.search(db, 'id', id)


def get_all():
  return db
