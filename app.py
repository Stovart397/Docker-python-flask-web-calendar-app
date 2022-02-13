from flask import Flask, render_template

app = Flask('FullCalendar Demo')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')