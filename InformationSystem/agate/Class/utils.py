import datetime

def get_new_id(db):
  count = len(db)
  if count == 0:
    return 1

  return db[count - 1]['id'] + 1

def search(db, key, value):
  for dict in db:
    print(dict[key], value)
    if dict[key] == value:
      return dict
  return {}

def searches(db, key, value):
  result = []
  for dict in db:
    print(dict[key], value)
    if dict[key] == value:
      result.append(dict)
  return result

def update(db, id, update_data):
  dict = search(db, 'id', id)
  for key in update_data:
    dict[key] = update_data[key]


date_format = ("%Y/%m/%d")

def get_today():
  return datetime.datetime.today().strftime(date_format)


def get_day_after(day):
  return (datetime.datetime.today() +
          datetime.timedelta(days=day)).strftime(date_format)
