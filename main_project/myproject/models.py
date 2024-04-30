from main_project.myproject import db

class Puppy(db.Model):
    __tablename__ = 'puppy'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and  owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner assigned yet."


class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return '<Owner name %r>' % self.name