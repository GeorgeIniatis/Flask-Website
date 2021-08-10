from market import db
from market.models import User, Item

db.drop_all()
db.create_all()  # Creates DB/overwrites existing one

users = [
    {"id": 1, "username": "Jorge", "email": "jogeo98@hotmail.com", "password": "123456"}
]

for user in users:
    user_entry = User(id=user["id"], username=user["username"], email=user["email"],
                      password=user["password"])
    # print(user_entry)
    db.session.add(user_entry)
    db.session.commit()

items = [
    {"id": 1, "name": "Phone", "barcode": "951475621452", "price": 450, "description": "A great phone"},
    {"id": 2, "name": "Laptop", "barcode": "914756248597", "price": 1200, "description": "High-end laptop"},
    {"id": 3, "name": "Headset", "barcode": "475614785234", "price": 300, "description": "Good headset of xbox"}
]

for item in items:
    item_entry = Item(id=item["id"], name=item["name"], barcode=item["barcode"], price=item["price"],
                      description=item["description"])  # Creates item object
    # print(item_entry)
    db.session.add(item_entry)  # Adds it to db temporarily
    db.session.commit()  # Commits the change to db permanently

phone = Item.query.filter_by(name="Phone").first()
phone.owner = User.query.filter_by(username="Jorge").first().id
db.session.commit()

print()
users = User.query.all()
print(users)
items = Item.query.all()
print(items)
