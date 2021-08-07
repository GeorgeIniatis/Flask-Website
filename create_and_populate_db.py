from market.models import *
from market import db

db.create_all()  # Creates DB/overwrites existing one

items = [
    {"id": 0, "name": "Phone", "barcode": "951475621452", "price": 450, "description": "A great phone"},
    {"id": 1, "name": "Laptop", "barcode": "914756248597", "price": 1200, "description": "High-end laptop"},
    {"id": 2, "name": "Headset", "barcode": "475614785234", "price": 300, "description": "Good headset of xbox"}
]

for item in items:
    item_entry = ItemModel(id=item["id"], name=item["name"], barcode=item["barcode"], price=item["price"],
                           description=item["description"])  # Creates item object
    print(item_entry)
    db.session.add(item_entry)  # Adds it to db temporarily
    db.session.commit()  # Commits the change to db permanently