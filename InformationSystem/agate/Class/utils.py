import datetime


def get_new_id(db):
  count = len(db)
  if count == 0:
    return 1

  return db[count - 1]['id'] + 1


def search(dict_list, key, value):
  for dict in dict_list:
    print(dict[key], value)
    if dict[key] == value:
      return dict
  return {}


def searches(dict_list, key, value):
  result = []
  for dict in dict_list:
    print(dict[key], value)
    if dict[key] == value:
      result.append(dict)
  return result


date_format = ("%Y/%m/%d")


def get_today():
  return datetime.datetime.today().strftime(date_format)


def get_day_after(day):
  return (datetime.datetime.today() +
          datetime.timedelta(days=day)).strftime(date_format)
