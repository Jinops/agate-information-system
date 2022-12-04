from Class import Client

Client.add_client(Client.Client(1, "테스트", ""))
Client.add_client(Client.Client(1, "테스트2", ""))
Client.add_client(Client.Client(1, "테스트3", ""))

print(Client.get_all_client())
print(Client.get_client(2))

c = Client.Client(1, "테4","")
Client.add_client(c)
print(Client.get_all_client())