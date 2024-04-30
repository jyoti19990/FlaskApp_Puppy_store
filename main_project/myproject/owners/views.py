from flask import render_template, redirect, url_for, Blueprint
from main_project.myproject import db
from main_project.myproject.owners.forms import AddOwnerForm
from main_project.myproject.models import Owner
owner_view = Blueprint('owners', __name__, template_folder='templates/owner')


@owner_view.route('/add', methods=['GET', 'POST'])
def add():
   form = AddOwnerForm()
   if form.validate_on_submit():
       name = form.name.data
       puppy_id = form.puppy_id.data
       new_owner = Owner(name, puppy_id)
       db.session.add(new_owner)
       db.session.commit()
       return redirect(url_for('puppies.list'))
   return render_template('owner.html',form=form)