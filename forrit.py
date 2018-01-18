from bottle import *
import os

@route('/')
def index():
    return '<a href="about">About</a> <a href="bio">Biography</a> <a href="pic">Pictures</a>'
@route('/about')
def about():
    return 'Hér eru upplýsingar um Steve Jobs'
@route('/bio')
def bio():
    return 'Hér er Biography frá Steve Jobs'
@route('/pic')
def pic():
    return 'Hérna eru myndir frá lífi Steve Jobs'

run(host='0.0.0.0',port=os.environ.get('PORT'))
