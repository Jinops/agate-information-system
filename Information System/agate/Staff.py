from enum import Enum

class Staff_grade(Enum):
    STAFF = 1
    CONTACT_STAFF = 2
    CAMPAIGN_STAFF = 3
    ACCOUNTANT = 4

class Staff:
    id:int
    name:int
    tel_number:str
    grade:Staff_grade
