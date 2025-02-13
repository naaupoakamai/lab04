import json

with open("/Users/azamatabilda/Desktop/PP2/lab04/json/sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 50)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU'}")
print("-" * 50)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    description = attributes.get("descr", "")

    print(f"{dn:<50} {description:<20} {speed:<10} {mtu}")
