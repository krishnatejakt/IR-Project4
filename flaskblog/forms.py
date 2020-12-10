from wtforms import Form, StringField, SelectField, SubmitField
from flask_wtf import FlaskForm

# class POISearchForm(Form):
#     choices = [('Modi', 'Modi'),
#                ('Trump', 'Trump'),
#                ('Amit', 'Amit')]
#     select = SelectField('Search for POI:', choices=choices)
#     search = StringField('')

class covid(FlaskForm):
    search = StringField('Query')
    
    choices = [('',''),('India','India'),('USA','USA'),('Italy','Italy')]
    select = SelectField('Country', choices=choices)

    choices1 = [('',''),('narendramodi','narendramodi'), ('VP','VP'),('joebiden','joebiden'),('pmoindia','pmoindia'),('smritiirani','smritiirani'),('realdonaldtrump','realdonaldtrump'),('AmitShah','AmitShah'),('matteosalvinimi','matteosalvinimi'),('cdcgov','cdcgov'),('ewarren','ewarren'),('giuseppeconte','giuseppeconte'),('nygovcuomo','nygovcuomo')]
    select1 = SelectField('POIs', choices=choices1)

    button_submit = SubmitField('Search')

class poi_names(FlaskForm):
    choices = [('',''),('narendramodi','narendramodi'), ('VP','VP'),('joebiden','joebiden'),('pmoindia','pmoindia'),('smritiirani','smritiirani'),('realdonaldtrump','realdonaldtrump'),('AmitShah','AmitShah'),('matteosalvinimi','matteosalvinimi'),('cdcgov','cdcgov'),('ewarren','ewarren'),('giuseppeconte','giuseppeconte'),('nygovcuomo','nygovcuomo')]
    select = SelectField('Search for POI:', choices=choices)
    button_submit = SubmitField('Search')

class country(FlaskForm):
    choices = [('',''),('India','India'),('USA','USA'),('Italy','Italy')]
    select = SelectField('Search for POI:', choices=choices)
    button_submit = SubmitField('Search')

class topic(FlaskForm):
    topics = [('',''),('a','a'),('b','b')]
    select = SelectField('Search for POI:', choices=topics)
    button_submit = SubmitField('Search')
