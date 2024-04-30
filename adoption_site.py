import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm,AddOwnerForm

app = Flask(__name__,static_url_path='/static')
app.config['SECRET_KEY'] = 'mykey'

###############DB Connection Sections################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'puppy_database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


##############Models#################
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


############## Views ####################

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        pup = Puppy(name)
        db.session.add(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():
    pups = Puppy.query.all()

    return render_template('list.html', pups=pups)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)
@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
   form = AddOwnerForm()
   if form.validate_on_submit():
       name = form.name.data
       puppy_id = form.puppy_id.data
       new_owner = Owner(name, puppy_id)
       db.session.add(new_owner)
       db.session.commit()
       return redirect(url_for('list_pup'))
   return render_template('owner.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)
