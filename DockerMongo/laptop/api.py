# Laptop Service
from flask import Flask, redirect, url_for, request, render_template
from flask_restful import Resource, Api
from pymongo import MongoClient
import flask, acp_times, arrow

# Instantiate the app
app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://admin:543219876@ds147518.mlab.com:47518/controle_times")
db = client.controle_times

time_list = []

'''
class Laptop(Resource):
    def get(self):
        return {
            'Laptops': ['Mac OS', 'Dell', 
            'Windozzee',
	    'Yet another laptop!',
	    'Yet yet another laptop!'
            ]
        }

# Create routes
# Another way, without decorators
api.add_resource(Laptop, '/')
'''

@app.route('/')
def calc():
    
    return flask.render_template('calc.html')

@app.route('/_calc_times')
def _calc_times():
    """
        Calculates open/close times from miles, using rules
        described at https://rusa.org/octime_alg.html.
        Expects one URL-encoded argument, the number of miles.
        """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    dist = request.args.get('dist', 1000, type=int)
    begin_date = request.args.get('begin_date')
    begin_time = request.args.get('begin_time')
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    open_time = acp_times.open_time(km, dist, arrow.get(('{} {}'.format(str(begin_date), str(begin_time))), 'YYYY-MM-DD HH:mm'))
    close_time = acp_times.close_time(km, dist, arrow.get(('{} {}'.format(str(begin_date), str(begin_time))), 'YYYY-MM-DD HH:mm'))
    result = {"open": open_time, "close": close_time}
    time_list.append(result)
    return flask.jsonify(result=result)


@app.route('/new')
def new():
    
    for item in time_list:
        item_doc = {
            'open_time': item['open'],
            'close_time': item['close']
        }
        db.acpTimes.insert_one(item_doc)

    time_list.clear()
    return redirect(url_for('calc'))

@app.route('/show')
def show():
    
    _items = db.acpTimes.find()
    items = [item for item in _items]
    
    return flask.render_template('elements.html', items=items)

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404

@app.errorhandler(500)
def error_500(e):
    app.logger.warning("++ 500 error: {}".format(e))
    assert not True  # I want to invoke the debugger
    return flask.render_template('500.html'), 500

@app.errorhandler(403)
def error_403(e):
    app.logger.warning("++ 403 error: {}".format(e))
    return flask.render_template('403.html'), 403


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
