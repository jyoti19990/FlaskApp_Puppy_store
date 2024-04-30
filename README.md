# FlaskApp_Puppy_store

1.install python 3.11

PreRequisite 

Install below python package with PIP command

install Flask  -3.0.3

3.install Flask-WTF -1.2.1

4.install Flask-SQLAlchemy -3.1.1

5.install Flask-Migrate -4.0.7

6.Install WTForms -3.1.2

7.install SQLAlchemy-2.0.29

---------------------------------------
for update database table using migration Migration

set FLASK_APP = app.py - window 

export FLASK_APP = app.py -linux

flask db init -> set up the migration directory

flask db migrate -m "comment" -> set up the migration file , you will be seeing migration folder after running this command

flask db upgrade -> update the database with the migration


RUN APP 

flask run 
