from market import db

# Specify db model/table
class ItemModel(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=100), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)

    def __repr__(self):
        return f"Item(id = {self.id}, name = {self.name}, barcode = {self.barcode}, price = {self.price}, description = {self.description} )"

