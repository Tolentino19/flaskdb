from wtforms import Form, StringField, validators

class PersonForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    phone = StringField('Phone', [validators.Length(min=6, max=35)])
