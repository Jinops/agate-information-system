def get_new_id(db):
    count = len(db)
    if count == 0:
        return 1
    
    return db[count-1]['id'] + 1

def search(dict_list, key, value):
    for dict in dict_list:
        print(dict[key], value)
        if dict[key] == value:
            return dict
    return {}