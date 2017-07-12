from flask import Flask, render_template, url_for, request, redirect, flash
from Flaskdb import app
from .person import db, Person
from .personforms import PersonForm

@app.route('/')
def index():
        persons = Person.query.all()
        return render_template('index.html', persons=persons)

@app.route('/create', methods=['GET','POST'])
def create():
        form = PersonForm(request.form)
        if request.method == 'POST' and form.validate():
                person = Person(form.name.data, form.phone.data)
                if Person.query.filter_by(name=person.name).first():
                        flash('Person already exists')
                        return redirect(url_for('create'))
			
                else:
                        db.session.add(person)
                        db.session.commit()
                        flash('Person added to phonebook.')
                        return redirect(url_for('index'))
        return render_template('create.html', form=form)
