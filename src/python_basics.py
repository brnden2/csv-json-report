# Python Basics Practice

# 1. Variables
name = "Brenden"
company = "DRS Global"
year = 2026

print("Name:", name)
print("Company:", company)
print("Year:", year)

print("--------------------")

# 2. List
clients = ["Client A", "Client B", "Client C"]

print("Clients:")
for client in clients:
    print(client)

print("--------------------")

# 3. Dictionary
client_info = {
    "name": "Client A",
    "package": "Hosting",
    "status": "Active"
}

print("Client Information:")
print("Name:", client_info["name"])
print("Package:", client_info["package"])
print("Status:", client_info["status"])