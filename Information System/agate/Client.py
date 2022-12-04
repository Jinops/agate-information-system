import db

class Client:
    id:int
    staff_id:int
    name:str
    tel_number:str

    def __init__(self, staff_id, name, tel_number):
        self.id = 0
        self.staff_id = staff_id
        self.name = name
        self.tel_number = tel_number
