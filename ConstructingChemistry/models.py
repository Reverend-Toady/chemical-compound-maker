from .app import db

class Compound(db.Model): # type: ignore
    cid = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(255), unique= True)
    formula = db.Column(db.String(255))
    weight = db.Column(db.Float)
    atoms = db.Column(db.LargeBinary)
    bonds = db.Column(db.LargeBinary)
    image = db.Column(db.LargeBinary)
