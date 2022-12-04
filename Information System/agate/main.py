import Staff
import Client
import Campaign
import Advert

import db

test_client = Client.Client(1, "테스트", "010-0000-1234")

test_client.add_client()

print("저장:", db.client[0].dict())