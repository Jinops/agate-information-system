from typing import Optional
from . import utils

class Client:
    id:Optional[int]
    staff_id:int
    name:str
    tel_number:str

    def __init__(self, staff_id, name, tel_number):
        self.staff_id = staff_id
        self.name = name
        self.tel_number = tel_number


db = [] # dictionary list

def add_client(client):
    client_dict = vars(client)
    client_dict['id'] = utils.get_new_id(db)
    db.append(client_dict)

def get_client(id: int):
    return utils.search(db, 'id', id)

def get_all_client():
    return db
