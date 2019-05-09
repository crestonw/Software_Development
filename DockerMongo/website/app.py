from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://admin:543219876@ds147518.mlab.com:47518/controle_times")

db = client.controle_times

@app.route('/')
def todo():

    render_template('todo.html')

@app.route('/new', methods=['POST'])
def new():
    item_doc = {
        'open_time': request.form['open'],
        'close_time': request.form['close']
    }
    db.acpTimes.insert_one(item_doc)

    return redirect(url_for('todo'))

@app.route('/show', methods=['POST'])
def show():
    
    _items = db.acpTimes.find()
    items = [item for item in _items]
    
    return render_template('elements.html', items=items)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
