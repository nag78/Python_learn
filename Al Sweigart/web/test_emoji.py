# -*- coding: cp1251 -*-

# from emoji import emojize

# print(emojize(":thumbs_up:").encode("cp1251"))
# import requests
# import pprint

# url = 'https://randomuser.me/api/?results=1'
# users = requests.get(url).json()
# users = str(users)

# pprint.pprint(users)

import uuid

user_id = uuid.uuid4()

print(user_id)