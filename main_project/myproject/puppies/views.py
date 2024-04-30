from flask import render_template, redirect, url_for, Blueprint
from main_project.myproject import db
from main_project.myproject.puppies.forms import AddForm,DelForm
from main_project.myproject.models import Puppy


puppies_blueprint = Blueprint('puppies',__name__,template_folder='templates/puppies')

@puppies_blueprint.route('/add', methods=['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        pup = Puppy(name)
        db.session.add(pup)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('add.html', form=form)

@puppies_blueprint.route('/list')
def list():
    pups = Puppy.query.all()

    return render_template('list.html', pups=pups)

@puppies_blueprint.route('/delete', methods=['GET','POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('delete.html', form=form)
