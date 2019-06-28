from app import app
from flask import render_template, request
from app.models import model, formopener

import random

@app.route('/')
@app.route('/index')
def index():
    result = model.next_launch()
    launch_date = result['launch_date_utc']
    return render_template('index.html', launch_date=launch_date)

@app.route('/next-launch')
def next_launch():
    result = model.next_launch()
    
    launch_date =result['launch_date_utc']
    rocket_name = result['rocket']['rocket_name']
    site_name_long =result['launch_site']['site_name_long']
    return render_template('next-launch.html', launch_date=launch_date, rocket_name=rocket_name, site_name_long=site_name_long)

@app.route('/last-launch')
def last_launch():
    last_result = model.last_launch()
    
    last_wiki = last_result['links']['wikipedia']
    last_youtube = last_result['links']['youtube_id']
    last_launch_date =last_result['launch_date_utc']
    last_rocket_name =last_result['rocket']['rocket_name']
    last_site_name_long =last_result['launch_site']['site_name_long']
    return render_template('last-launch.html', last_launch_date=last_launch_date, last_rocket_name=last_rocket_name, last_site_name_long=last_site_name_long, last_wiki=last_wiki, last_youtube=last_youtube)

@app.route('/next-countdown')
def next_countdown():
    result = model.next_launch()
    launch_date = result['launch_date_utc']
    return render_template('next-countdown.html', launch_date=launch_date)

@app.route('/previous-launches')
def previous_launches():
    flights_info = {}
    
    past_result = model.past_launches()
    rand_num = random.randint(1, 82)
    
    past_wiki1 = past_result[rand_num]['links']['wikipedia']
    past_youtube1 = past_result[rand_num]['links']['youtube_id']
    past_launch_date1 =past_result[rand_num]['launch_date_utc']
    past_rocket_name1 =past_result[rand_num]['rocket']['rocket_name']
    past_site_name_long1 =past_result[rand_num]['launch_site']['site_name_long']
    
    rand_num1 = random.randint(1, 82)
    past_wiki2 = past_result[rand_num1]['links']['wikipedia']
    past_youtube2 = past_result[rand_num1]['links']['youtube_id']
    past_launch_date2 =past_result[rand_num1]['launch_date_utc']
    past_rocket_name2 =past_result[rand_num1]['rocket']['rocket_name']
    past_site_name_long2 =past_result[rand_num1]['launch_site']['site_name_long']
    
    return render_template('previous-launches.html', past_wiki2=past_wiki2, past_site_name_long1=past_site_name_long1, past_site_name_long2=past_site_name_long2, past_rocket_name1=past_rocket_name1, past_rocket_name2=past_rocket_name2, past_launch_date1=past_launch_date1, past_launch_date2= past_launch_date2, past_youtube1=past_youtube1, past_youtube2=past_youtube2, past_wiki1=past_wiki1)
