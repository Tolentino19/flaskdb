from flask import Flask, render_template, url_for, request, redirect, flash, session, g
from Flaskdb import app
from functools import wraps
from .person import db, Person
from .personforms import PersonForm


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
                if session['logged_in'] == False:
                        return redirect(url_for('login', next=request.url))
        except KeyError:
                return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

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

@app.route('/teste')
@login_required
def teste():
        flash('Done!')
        return redirect(url_for('index'))

@app.route('/login')
def login():
        session['logged_in'] = True      
